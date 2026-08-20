"""
Skill Gap Engine
----------------

Compares a student's current skill profile with the
structured requirements of a selected career.

Works with:

    src/skill_data.py
    src/student_skills.py

The engine identifies:

    1. Current skill strengths
    2. Skills that need development
    3. High / medium / low priority gaps
    4. Skills requiring more information
    5. Overall skill readiness
    6. Skill evidence coverage

IMPORTANT:

    UNKNOWN != NONE

UNKNOWN
    We do not have enough information about the skill.

NONE
    The student explicitly has no experience with the skill.

Therefore:

    UNKNOWN → missing information
    NONE    → actual development gap

This engine does NOT determine career eligibility.
It provides developmental guidance only.
"""


# ============================================================
# IMPORTS
# ============================================================

from skill_data import (
    CAREER_SKILLS,
    SKILL_IMPORTANCE,
    validate_skill_data,
)

from student_skills import (
    create_student_skill_profile,
    validate_student_skill_profile,
)


# ============================================================
# STUDENT SKILL LEVELS
# ============================================================
#
# IMPORTANT:
#
# These are STUDENT levels.
#
# "unknown" belongs here because a student may not have
# provided information about a particular skill.
#
# We intentionally do NOT modify skill_data.py.
#

STUDENT_SKILL_LEVELS = {
    "unknown": -1,
    "none": 0,
    "foundational": 1,
    "beginner": 2,
    "intermediate": 3,
    "advanced": 4,
}


UNKNOWN_LEVEL = "unknown"


# ============================================================
# LEVEL NORMALIZATION
# ============================================================

def normalize_skill_level(level):
    """
    Normalize and validate a student's skill level.

    Supported values:

        unknown
        none
        foundational
        beginner
        intermediate
        advanced
    """

    if level is None:
        return UNKNOWN_LEVEL

    if not isinstance(level, str):
        raise ValueError(
            "Skill level must be a string."
        )

    normalized = (
        level
        .strip()
        .lower()
    )

    if normalized not in STUDENT_SKILL_LEVELS:
        raise ValueError(
            f"Invalid skill level: {level}. "
            f"Allowed values: "
            f"{list(STUDENT_SKILL_LEVELS.keys())}"
        )

    return normalized


# ============================================================
# LEVEL VALUE
# ============================================================

def get_level_value(level):
    """
    Convert a student skill level into a numerical value.

    unknown = -1
    none = 0
    foundational = 1
    beginner = 2
    intermediate = 3
    advanced = 4
    """

    normalized = normalize_skill_level(
        level
    )

    return STUDENT_SKILL_LEVELS[
        normalized
    ]


# ============================================================
# SKILL STATUS
# ============================================================

def classify_skill_status(
    current_level,
    expected_level,
):
    """
    Compare the student's current level with the career's
    expected level.

    Returns:

        unknown
        strong
        adequate
        developing
        gap
    """

    current_level = normalize_skill_level(
        current_level
    )

    # --------------------------------------------------------
    # Unknown student information
    # --------------------------------------------------------

    if current_level == UNKNOWN_LEVEL:
        return "unknown"

    # --------------------------------------------------------
    # Career requirements should never be unknown.
    #
    # Career levels come from skill_data.py and therefore
    # should be one of:
    #
    # foundational
    # beginner
    # intermediate
    # advanced
    # --------------------------------------------------------

    if (
        expected_level is None
        or expected_level == UNKNOWN_LEVEL
    ):
        return "unknown"

    if expected_level not in STUDENT_SKILL_LEVELS:
        raise ValueError(
            f"Invalid expected career skill level: "
            f"{expected_level}"
        )

    current_value = get_level_value(
        current_level
    )

    expected_value = get_level_value(
        expected_level
    )

    # --------------------------------------------------------
    # Above expectation
    # --------------------------------------------------------

    if current_value > expected_value:
        return "strong"

    # --------------------------------------------------------
    # Exactly meets expectation
    # --------------------------------------------------------

    if current_value == expected_value:
        return "adequate"

    # --------------------------------------------------------
    # Below expectation
    # --------------------------------------------------------

    difference = (
        expected_value
        - current_value
    )

    if difference == 1:
        return "developing"

    return "gap"


# ============================================================
# GAP PRIORITY
# ============================================================

def determine_gap_priority(
    current_level,
    expected_level,
    importance,
):
    """
    Determine development priority.

    Returns:

        High
        Medium
        Low
        None

    Unknown skills receive no priority because we first
    need more information.
    """

    current_level = normalize_skill_level(
        current_level
    )

    if (
        expected_level is None
        or expected_level == UNKNOWN_LEVEL
    ):
        return "None"

    if current_level == UNKNOWN_LEVEL:
        return "None"

    if importance not in SKILL_IMPORTANCE:
        raise ValueError(
            f"Unknown skill importance: "
            f"{importance}"
        )

    current_value = get_level_value(
        current_level
    )

    expected_value = get_level_value(
        expected_level
    )

    gap = (
        expected_value
        - current_value
    )

    # --------------------------------------------------------
    # No gap
    # --------------------------------------------------------

    if gap <= 0:
        return "None"

    importance_value = (
        SKILL_IMPORTANCE[
            importance
        ]
    )

    # --------------------------------------------------------
    # Core skill
    # --------------------------------------------------------

    if importance_value == 3:

        if gap >= 2:
            return "High"

        return "Medium"

    # --------------------------------------------------------
    # Important skill
    # --------------------------------------------------------

    if importance_value == 2:

        if gap >= 2:
            return "Medium"

        return "Low"

    # --------------------------------------------------------
    # Supporting skill
    # --------------------------------------------------------

    return "Low"


# ============================================================
# BUILD SINGLE SKILL RESULT
# ============================================================

def build_skill_result(
    skill_id,
    requirement,
    student_entry,
):
    """
    Build the analysis for one career-required skill.
    """

    expected_level = (
        requirement[
            "expected_level"
        ]
    )

    # --------------------------------------------------------
    # Student information
    # --------------------------------------------------------

    if student_entry is None:

        current_level = UNKNOWN_LEVEL

        evidence = []

        evidence_strength = None

    else:

        current_level = normalize_skill_level(
            student_entry.get(
                "level",
                UNKNOWN_LEVEL,
            )
        )

        evidence = student_entry.get(
            "evidence",
            [],
        )

        evidence_strength = (
            student_entry.get(
                "evidence_strength"
            )
        )

    # --------------------------------------------------------
    # Status
    # --------------------------------------------------------

    status = classify_skill_status(
        current_level,
        expected_level,
    )

    # --------------------------------------------------------
    # Priority
    # --------------------------------------------------------

    priority = determine_gap_priority(
        current_level,
        expected_level,
        requirement[
            "importance"
        ],
    )

    # --------------------------------------------------------
    # Numerical values
    # --------------------------------------------------------

    current_value = get_level_value(
        current_level
    )

    expected_value = get_level_value(
        expected_level
    )

    # --------------------------------------------------------
    # Gap
    # --------------------------------------------------------
    #
    # Unknown does NOT have a numerical gap.
    #

    if current_level == UNKNOWN_LEVEL:

        gap = None

    else:

        gap = max(
            expected_value
            - current_value,
            0,
        )

    return {

        "skill_id": skill_id,

        "category": requirement[
            "category"
        ],

        "importance": requirement[
            "importance"
        ],

        "current_level": current_level,

        "expected_level": expected_level,

        "current_value": current_value,

        "expected_value": expected_value,

        "gap": gap,

        "status": status,

        "priority": priority,

        "evidence": evidence,

        "evidence_strength": (
            evidence_strength
        ),
    }


# ============================================================
# READINESS CALCULATION
# ============================================================

def calculate_known_skill_readiness(
    skill_results,
):
    """
    Calculate skill readiness using only known skills.

    Unknown skills are excluded from the readiness
    calculation.

    This prevents missing information from being
    interpreted as poor ability.

    Returns:

        readiness percentage
        evidence coverage percentage
    """

    known_results = [
        item
        for item in skill_results
        if item["status"] != "unknown"
    ]

    total_known_weight = 0.0

    achieved_weight = 0.0

    for item in known_results:

        importance_weight = (
            SKILL_IMPORTANCE[
                item["importance"]
            ]
        )

        expected_value = (
            item["expected_value"]
        )

        current_value = min(
            item["current_value"],
            expected_value,
        )

        total_known_weight += (
            expected_value
            * importance_weight
        )

        achieved_weight += (
            current_value
            * importance_weight
        )

    # --------------------------------------------------------
    # No known skills
    # --------------------------------------------------------

    if total_known_weight == 0:

        readiness = 0.0

    else:

        readiness = (
            achieved_weight
            / total_known_weight
        ) * 100

    # --------------------------------------------------------
    # Evidence coverage
    # --------------------------------------------------------

    if len(skill_results) == 0:

        evidence_coverage = 0.0

    else:

        evidence_coverage = (
            len(known_results)
            / len(skill_results)
        ) * 100

    return (
        round(readiness, 2),
        round(evidence_coverage, 2),
    )


# ============================================================
# COMPLETE SKILL GAP CALCULATION
# ============================================================

def calculate_skill_gap(
    career_id,
    student_profile,
):
    """
    Calculate the skill gap between a student and career.

    Parameters
    ----------
    career_id : str
        Career ID from CAREER_SKILLS.

    student_profile : dict
        Student skill profile created by
        create_student_skill_profile().

    Returns
    -------
    dict
        Complete skill gap report.
    """

    # --------------------------------------------------------
    # Validate career
    # --------------------------------------------------------

    if career_id not in CAREER_SKILLS:

        raise ValueError(
            f"Unknown career ID: "
            f"{career_id}"
        )

    # --------------------------------------------------------
    # Validate student profile
    # --------------------------------------------------------

    validate_student_skill_profile(
        student_profile
    )

    career = CAREER_SKILLS[
        career_id
    ]

    required_skills = career[
        "skills"
    ]

    student_skills = (
        student_profile[
            "skills"
        ]
    )

    # --------------------------------------------------------
    # Analyze all career-required skills
    # --------------------------------------------------------

    all_results = []

    for skill_id, requirement in (
        required_skills.items()
    ):

        student_entry = (
            student_skills.get(
                skill_id
            )
        )

        result = build_skill_result(
            skill_id,
            requirement,
            student_entry,
        )

        all_results.append(
            result
        )

    # ========================================================
    # CATEGORIZE RESULTS
    # ========================================================

    current_strengths = [
        item
        for item in all_results
        if item["status"]
        in (
            "strong",
            "adequate",
        )
    ]

    growth_opportunities = [
        item
        for item in all_results
        if item["status"]
        in (
            "developing",
            "gap",
        )
    ]

    unknown_skills = [
        item
        for item in all_results
        if item["status"]
        == "unknown"
    ]

    high_priority_gaps = [
        item
        for item in growth_opportunities
        if item["priority"]
        == "High"
    ]

    medium_priority_gaps = [
        item
        for item in growth_opportunities
        if item["priority"]
        == "Medium"
    ]

    low_priority_gaps = [
        item
        for item in growth_opportunities
        if item["priority"]
        == "Low"
    ]

    # ========================================================
    # READINESS
    # ========================================================

    (
        readiness,
        evidence_coverage,
    ) = calculate_known_skill_readiness(
        all_results
    )

    # ========================================================
    # FINAL REPORT
    # ========================================================

    return {

        "career_id": career_id,

        "career_name": career[
            "career_name"
        ],

        "student_mode": student_profile[
            "student_mode"
        ],

        "overall_skill_readiness": readiness,

        "skill_evidence_coverage": (
            evidence_coverage
        ),

        "total_required_skills": len(
            all_results
        ),

        "known_skills": len(
            all_results
        ) - len(
            unknown_skills
        ),

        "unknown_skills": len(
            unknown_skills
        ),

        "skills_meeting_expectation": len(
            current_strengths
        ),

        "skills_needing_development": len(
            growth_opportunities
        ),

        "current_strengths": (
            current_strengths
        ),

        "growth_opportunities": (
            growth_opportunities
        ),

        "high_priority_gaps": (
            high_priority_gaps
        ),

        "medium_priority_gaps": (
            medium_priority_gaps
        ),

        "low_priority_gaps": (
            low_priority_gaps
        ),

        "needs_more_information": (
            unknown_skills
        ),

        "all_skills": all_results,
    }


# ============================================================
# DISPLAY HELPERS
# ============================================================

def format_skill_name(skill_id):
    """
    Convert an internal skill ID to a readable name.
    """

    return (
        skill_id
        .replace("_", " ")
        .strip()
        .title()
    )


def format_level(level):
    """
    Convert an internal level into a user-friendly label.
    """

    labels = {

        "unknown": "Not enough information",

        "none": "No experience",

        "foundational": "Foundational",

        "beginner": "Beginner",

        "intermediate": "Intermediate",

        "advanced": "Advanced",
    }

    return labels.get(
        level,
        level,
    )


# ============================================================
# PRINT SKILL LIST
# ============================================================

def print_skill_list(
    title,
    items,
):
    """
    Print a readable list of skills.
    """

    print()

    print(title)

    if not items:

        print(
            "  - None"
        )

        return

    for item in items:

        skill_name = (
            format_skill_name(
                item["skill_id"]
            )
        )

        current = format_level(
            item["current_level"]
        )

        expected = format_level(
            item["expected_level"]
        )

        print(
            f"  - {skill_name}: "
            f"{current}"
        )

        # ----------------------------------------------------
        # Growth information
        # ----------------------------------------------------

        if item["status"] in (
            "developing",
            "gap",
        ):

            print(
                f"      Target: "
                f"{expected}"
            )

            print(
                f"      Priority: "
                f"{item['priority']}"
            )

        # ----------------------------------------------------
        # Evidence
        # ----------------------------------------------------

        if item["evidence"]:

            print(
                "      Evidence:"
            )

            for evidence_item in (
                item["evidence"]
            ):

                print(
                    f"        - "
                    f"{evidence_item}"
                )


# ============================================================
# PRINT COMPLETE REPORT
# ============================================================

def print_skill_gap_report(
    report,
):
    """
    Print a student-friendly skill-gap report.
    """

    print()

    print(
        "=" * 80
    )

    print(
        report[
            "career_name"
        ]
    )

    print(
        "=" * 80
    )

    print(
        f"Student mode: "
        f"{report['student_mode']}"
    )

    print(
        f"Skill readiness: "
        f"{report['overall_skill_readiness']:.1f}%"
    )

    print(
        f"Evidence coverage: "
        f"{report['skill_evidence_coverage']:.1f}%"
    )

    # --------------------------------------------------------
    # Strengths
    # --------------------------------------------------------

    print_skill_list(
        "Skills currently meeting expectations:",
        report[
            "current_strengths"
        ],
    )

    # --------------------------------------------------------
    # High priority
    # --------------------------------------------------------

    print_skill_list(
        "High-priority skills to develop:",
        report[
            "high_priority_gaps"
        ],
    )

    # --------------------------------------------------------
    # Medium priority
    # --------------------------------------------------------

    print_skill_list(
        "Medium-priority skills to develop:",
        report[
            "medium_priority_gaps"
        ],
    )

    # --------------------------------------------------------
    # Low priority
    # --------------------------------------------------------

    print_skill_list(
        "Lower-priority skills to develop:",
        report[
            "low_priority_gaps"
        ],
    )

    # --------------------------------------------------------
    # Unknown
    # --------------------------------------------------------

    print()

    print(
        "Skills needing more information:"
    )

    unknown = report[
        "needs_more_information"
    ]

    if not unknown:

        print(
            "  - No additional information needed."
        )

    else:

        for item in unknown:

            skill_name = (
                format_skill_name(
                    item["skill_id"]
                )
            )

            print(
                f"  - {skill_name}"
            )

    # --------------------------------------------------------
    # Interpretation
    # --------------------------------------------------------

    print()

    print(
        "Interpretation:"
    )

    coverage = report[
        "skill_evidence_coverage"
    ]

    if coverage < 50:

        print(
            "  The skill assessment currently has "
            "limited information. Additional skill "
            "details would make the analysis more useful."
        )

    elif coverage < 80:

        print(
            "  The assessment has reasonable information, "
            "but some required skills have not yet been "
            "assessed."
        )

    else:

        print(
            "  The assessment has good information across "
            "most of the career's required skills."
        )


# ============================================================
# TEST STUDENT A
# ============================================================

STUDENT_A_SKILLS = {

    "python": {
        "level": "beginner",

        "evidence": [
            "Completed Python fundamentals"
        ],

        "evidence_strength": "supported",
    },

    "sql": {
        "level": "none",

        "evidence": [
            "Has not learned SQL yet"
        ],

        "evidence_strength": "supported",
    },

    "statistics": {
        "level": "foundational",

        "evidence": [
            "Studied introductory statistics"
        ],

        "evidence_strength": "supported",
    },

    "analytical_thinking": {
        "level": "intermediate",

        "evidence": [
            "Strong analytical performance"
        ],

        "evidence_strength": "strong",
    },

    "research": {
        "level": "beginner",

        "evidence": [
            "Has explored research topics"
        ],

        "evidence_strength": "supported",
    },

    # --------------------------------------------------------
    # Unknown skills
    # --------------------------------------------------------

    "probability": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "linear_algebra": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "pandas": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "data_visualization": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "machine_learning": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "data_cleaning": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "communication": {
        "level": "beginner",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "projects": {
        "level": "beginner",

        "evidence": [
            "Completed academic projects"
        ],

        "evidence_strength": "supported",
    },
}


# ============================================================
# TEST STUDENT B
# ============================================================

STUDENT_B_SKILLS = {

    "biology": {
        "level": "intermediate",

        "evidence": [
            "Studied biology"
        ],

        "evidence_strength": "supported",
    },

    "anatomy": {
        "level": "foundational",

        "evidence": [
            "Basic academic exposure"
        ],

        "evidence_strength": "supported",
    },

    "empathy": {
        "level": "intermediate",

        "evidence": [
            "Strong people-helping preference"
        ],

        "evidence_strength": "supported",
    },

    "patient_communication": {
        "level": "beginner",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "teamwork": {
        "level": "beginner",

        "evidence": [
            "Participated in group activities"
        ],

        "evidence_strength": "supported",
    },

    # --------------------------------------------------------
    # Unknown skills
    # --------------------------------------------------------

    "patient_care": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "attention_to_detail": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "decision_making": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "stress_management": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "clinical_skills": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },
}


# ============================================================
# VALIDATION
# ============================================================

def validate_skill_gap_engine():
    """
    Validate the complete skill-gap engine.
    """

    # --------------------------------------------------------
    # Validate career knowledge
    # --------------------------------------------------------

    validate_skill_data()

    # --------------------------------------------------------
    # Create Student A
    # --------------------------------------------------------

    student_a = (
        create_student_skill_profile(
            "college",
            STUDENT_A_SKILLS,
        )
    )

    # --------------------------------------------------------
    # Create Student B
    # --------------------------------------------------------

    student_b = (
        create_student_skill_profile(
            "school",
            STUDENT_B_SKILLS,
        )
    )

    # --------------------------------------------------------
    # Validate student profiles
    # --------------------------------------------------------

    validate_student_skill_profile(
        student_a
    )

    validate_student_skill_profile(
        student_b
    )

    # --------------------------------------------------------
    # Generate reports
    # --------------------------------------------------------

    report_a = calculate_skill_gap(
        "data_scientist",
        student_a,
    )

    report_b = calculate_skill_gap(
        "nurse",
        student_b,
    )

    if not report_a:

        raise ValueError(
            "Student A report was not generated."
        )

    if not report_b:

        raise ValueError(
            "Student B report was not generated."
        )

    # ========================================================
    # UNKNOWN HANDLING TEST
    # ========================================================

    unknown_found = any(
        item["status"] == "unknown"
        for item in report_a[
            "all_skills"
        ]
    )

    if not unknown_found:

        raise ValueError(
            "Unknown skill handling test failed."
        )

    # ========================================================
    # NONE HANDLING TEST
    # ========================================================

    sql_result = next(
        (
            item
            for item in report_a[
                "all_skills"
            ]
            if item["skill_id"]
            == "sql"
        ),
        None,
    )

    if sql_result is None:

        raise ValueError(
            "SQL test skill was not found."
        )

    if sql_result["status"] == "unknown":

        raise ValueError(
            "NONE skill was incorrectly treated "
            "as UNKNOWN."
        )

    # ========================================================
    # FINAL VALIDATION
    # ========================================================

    return True


# ============================================================
# MAIN TEST
# ============================================================

if __name__ == "__main__":

    validate_skill_gap_engine()

    print(
        "Skill-gap engine validation successful."
    )

    # ========================================================
    # STUDENT A
    # ========================================================

    student_a = (
        create_student_skill_profile(
            "college",
            STUDENT_A_SKILLS,
        )
    )

    report_a = calculate_skill_gap(
        "data_scientist",
        student_a,
    )

    print()

    print(
        "STUDENT A"
    )

    print_skill_gap_report(
        report_a
    )

    # ========================================================
    # STUDENT B
    # ========================================================

    student_b = (
        create_student_skill_profile(
            "school",
            STUDENT_B_SKILLS,
        )
    )

    report_b = calculate_skill_gap(
        "nurse",
        student_b,
    )

    print()

    print(
        "STUDENT B"
    )

    print_skill_gap_report(
        report_b
    )

    # ========================================================
    # FINAL STATUS
    # ========================================================

    print()

    print(
        "=" * 80
    )

    print(
        "Skill-gap engine test completed successfully."
    )

    print(
        "UNKNOWN skills are treated as missing information."
    )

    print(
        "NONE skills are treated as explicit development gaps."
    )