"""
Student Skill Profile
---------------------

Defines the structure used to represent a student's
current skills and supporting evidence.

This module does NOT calculate career matches.

It provides a clean input structure for the Skill-Gap Engine.

Skill state:

    unknown
        We do not have enough information yet.

    none
        Student has explicitly indicated no experience.

    foundational
        Basic awareness or academic exposure.

    beginner
        Can perform simple tasks with the skill.

    intermediate
        Can use the skill independently and/or in projects.

    advanced
        Strong practical experience with the skill.

Evidence strength:

    self_reported
        Student directly reports the skill.

    supported
        Student provides some supporting evidence.

    strong
        Multiple or substantial pieces of evidence support it.
"""


# ============================================================
# CONSTANTS
# ============================================================

SKILL_LEVELS = {
    "unknown": -1,
    "none": 0,
    "foundational": 1,
    "beginner": 2,
    "intermediate": 3,
    "advanced": 4,
}


EVIDENCE_STRENGTHS = {
    "self_reported": 1,
    "supported": 2,
    "strong": 3,
}


STUDENT_MODES = {
    "school",
    "college",
}


# ============================================================
# LEVEL DISPLAY NAMES
# ============================================================

SKILL_LEVEL_DISPLAY_NAMES = {

    "unknown": "Not enough information",

    "none": "No experience",

    "foundational": "Foundational",

    "beginner": "Beginner",

    "intermediate": "Intermediate",

    "advanced": "Advanced",
}


# ============================================================
# NORMALIZATION
# ============================================================

def normalize_skill_level(level):
    """
    Normalize and validate a skill level.

    Returns:
        Standardized lowercase skill level.
    """

    if level is None:
        return "unknown"

    if not isinstance(level, str):
        raise ValueError(
            "Skill level must be a string."
        )

    normalized = level.strip().lower()

    if normalized not in SKILL_LEVELS:
        raise ValueError(
            f"Invalid skill level: {level}. "
            f"Allowed values: "
            f"{list(SKILL_LEVELS.keys())}"
        )

    return normalized


def normalize_evidence_strength(
    evidence_strength,
):
    """
    Normalize and validate evidence strength.
    """

    if evidence_strength is None:
        return "self_reported"

    if not isinstance(
        evidence_strength,
        str,
    ):
        raise ValueError(
            "Evidence strength must be a string."
        )

    normalized = (
        evidence_strength
        .strip()
        .lower()
    )

    if normalized not in EVIDENCE_STRENGTHS:
        raise ValueError(
            f"Invalid evidence strength: "
            f"{evidence_strength}. "
            f"Allowed values: "
            f"{list(EVIDENCE_STRENGTHS.keys())}"
        )

    return normalized


def normalize_student_mode(mode):
    """
    Normalize and validate student mode.

    Supported modes:

        school
        college
    """

    if not isinstance(
        mode,
        str,
    ):
        raise ValueError(
            "Student mode must be a string."
        )

    normalized = (
        mode
        .strip()
        .lower()
    )

    if normalized not in STUDENT_MODES:
        raise ValueError(
            f"Invalid student mode: {mode}. "
            f"Allowed values: "
            f"{sorted(STUDENT_MODES)}"
        )

    return normalized


# ============================================================
# SKILL LEVEL VALUE
# ============================================================

def get_skill_level_value(level):
    """
    Convert a skill level into its numerical value.

    Unknown returns -1 because it represents missing
    information rather than zero ability.
    """

    normalized = normalize_skill_level(
        level
    )

    return SKILL_LEVELS[
        normalized
    ]


# ============================================================
# SKILL NAME
# ============================================================

def format_skill_name(skill_id):
    """
    Convert an internal skill ID into a readable name.

    Example:

        data_visualization
        ->
        Data Visualization
    """

    if not isinstance(
        skill_id,
        str,
    ):
        raise ValueError(
            "skill_id must be a string."
        )

    return (
        skill_id
        .replace("_", " ")
        .strip()
        .title()
    )


# ============================================================
# CREATE SINGLE SKILL ENTRY
# ============================================================

def create_skill_entry(
    level="unknown",
    evidence=None,
    evidence_strength="self_reported",
):
    """
    Create a single structured skill entry.

    Example:

        {
            "level": "intermediate",
            "evidence": [
                "Built two projects"
            ],
            "evidence_strength": "supported"
        }
    """

    normalized_level = (
        normalize_skill_level(
            level
        )
    )

    normalized_strength = (
        normalize_evidence_strength(
            evidence_strength
        )
    )

    if evidence is None:
        evidence = []

    if not isinstance(
        evidence,
        list,
    ):
        raise ValueError(
            "Evidence must be provided "
            "as a list."
        )

    cleaned_evidence = []

    for item in evidence:

        if not isinstance(
            item,
            str,
        ):
            raise ValueError(
                "Each evidence item must "
                "be a string."
            )

        cleaned_item = item.strip()

        if cleaned_item:
            cleaned_evidence.append(
                cleaned_item
            )

    # --------------------------------------------------------
    # Evidence consistency
    # --------------------------------------------------------
    #
    # If there is no actual evidence, the strongest possible
    # evidence state should remain self_reported.
    #
    # We do not automatically claim that a skill is
    # "supported" or "strong".
    #

    if (
        not cleaned_evidence
        and normalized_strength
        != "self_reported"
    ):
        normalized_strength = (
            "self_reported"
        )

    return {
        "level": normalized_level,
        "evidence": cleaned_evidence,
        "evidence_strength": (
            normalized_strength
        ),
    }


# ============================================================
# CREATE STUDENT SKILL PROFILE
# ============================================================

def create_student_skill_profile(
    student_mode,
    skills=None,
):
    """
    Create a complete student skill profile.

    Parameters
    ----------
    student_mode : str
        "school" or "college"

    skills : dict
        Dictionary containing skill entries.

    Example:

        {
            "python": {
                "level": "beginner",
                "evidence": [
                    "Completed Python basics"
                ],
                "evidence_strength": "supported"
            }
        }

    Returns
    -------
    dict
        Structured student skill profile.
    """

    normalized_mode = (
        normalize_student_mode(
            student_mode
        )
    )

    if skills is None:
        skills = {}

    if not isinstance(
        skills,
        dict,
    ):
        raise ValueError(
            "skills must be a dictionary."
        )

    profile_skills = {}

    for skill_id, skill_data in (
        skills.items()
    ):

        if not isinstance(
            skill_id,
            str,
        ):
            raise ValueError(
                "Skill IDs must be strings."
            )

        cleaned_skill_id = (
            skill_id.strip().lower()
        )

        if not cleaned_skill_id:
            raise ValueError(
                "Skill ID cannot be empty."
            )

        # ----------------------------------------------------
        # Allow simple format:
        #
        # "python": "beginner"
        #
        # This keeps the module convenient for testing.
        # ----------------------------------------------------

        if isinstance(
            skill_data,
            str,
        ):

            profile_skills[
                cleaned_skill_id
            ] = create_skill_entry(
                level=skill_data
            )

        # ----------------------------------------------------
        # Structured format:
        #
        # "python": {
        #     "level": "beginner",
        #     "evidence": [...],
        #     "evidence_strength": "supported"
        # }
        # ----------------------------------------------------

        elif isinstance(
            skill_data,
            dict,
        ):

            profile_skills[
                cleaned_skill_id
            ] = create_skill_entry(
                level=skill_data.get(
                    "level",
                    "unknown",
                ),
                evidence=skill_data.get(
                    "evidence",
                    [],
                ),
                evidence_strength=(
                    skill_data.get(
                        "evidence_strength",
                        "self_reported",
                    )
                ),
            )

        else:

            raise ValueError(
                f"Invalid skill data for "
                f"'{skill_id}'. "
                f"Expected a string or dictionary."
            )

    return {
        "student_mode": normalized_mode,
        "skills": profile_skills,
    }


# ============================================================
# ADD OR UPDATE SKILL
# ============================================================

def set_student_skill(
    profile,
    skill_id,
    level,
    evidence=None,
    evidence_strength="self_reported",
):
    """
    Add or update one skill in an existing profile.

    Returns the updated profile.
    """

    if not isinstance(
        profile,
        dict,
    ):
        raise ValueError(
            "profile must be a dictionary."
        )

    if "student_mode" not in profile:
        raise ValueError(
            "Profile is missing student_mode."
        )

    if "skills" not in profile:
        raise ValueError(
            "Profile is missing skills."
        )

    if not isinstance(
        skill_id,
        str,
    ):
        raise ValueError(
            "skill_id must be a string."
        )

    cleaned_skill_id = (
        skill_id.strip().lower()
    )

    if not cleaned_skill_id:
        raise ValueError(
            "skill_id cannot be empty."
        )

    profile["skills"][
        cleaned_skill_id
    ] = create_skill_entry(
        level=level,
        evidence=evidence,
        evidence_strength=evidence_strength,
    )

    return profile


# ============================================================
# GET SKILL ENTRY
# ============================================================

def get_student_skill(
    profile,
    skill_id,
):
    """
    Get one skill from the student's profile.

    Returns None if the skill has not been provided.
    """

    if not isinstance(
        profile,
        dict,
    ):
        raise ValueError(
            "profile must be a dictionary."
        )

    skills = profile.get(
        "skills",
        {},
    )

    return skills.get(
        skill_id.strip().lower()
    )


# ============================================================
# GET SKILL LEVEL
# ============================================================

def get_student_skill_level(
    profile,
    skill_id,
):
    """
    Return the student's level for a skill.

    If the skill has never been provided,
    return "unknown".
    """

    entry = get_student_skill(
        profile,
        skill_id,
    )

    if entry is None:
        return "unknown"

    return entry[
        "level"
    ]


# ============================================================
# GET EVIDENCE STRENGTH
# ============================================================

def get_student_skill_evidence_strength(
    profile,
    skill_id,
):
    """
    Return evidence strength for a skill.

    If the skill is unknown, return None.
    """

    entry = get_student_skill(
        profile,
        skill_id,
    )

    if entry is None:
        return None

    return entry[
        "evidence_strength"
    ]


# ============================================================
# UNKNOWN SKILLS
# ============================================================

def get_unknown_skills(
    profile,
):
    """
    Return skill IDs explicitly stored as unknown.
    """

    unknown = []

    for skill_id, entry in profile[
        "skills"
    ].items():

        if entry[
            "level"
        ] == "unknown":

            unknown.append(
                skill_id
            )

    return unknown


# ============================================================
# KNOWN SKILLS
# ============================================================

def get_known_skills(
    profile,
):
    """
    Return skills for which we have a known
    level, including "none".
    """

    known = []

    for skill_id, entry in profile[
        "skills"
    ].items():

        if entry[
            "level"
        ] != "unknown":

            known.append(
                skill_id
            )

    return known


# ============================================================
# PROFILE VALIDATION
# ============================================================

def validate_student_skill_profile(
    profile,
):
    """
    Validate the complete student skill profile.

    Returns True if valid.
    """

    if not isinstance(
        profile,
        dict,
    ):
        raise ValueError(
            "Student skill profile must "
            "be a dictionary."
        )

    if "student_mode" not in profile:
        raise ValueError(
            "Student skill profile is missing "
            "student_mode."
        )

    if "skills" not in profile:
        raise ValueError(
            "Student skill profile is missing "
            "skills."
        )

    normalize_student_mode(
        profile["student_mode"]
    )

    if not isinstance(
        profile["skills"],
        dict,
    ):
        raise ValueError(
            "Profile skills must be a dictionary."
        )

    for skill_id, entry in (
        profile["skills"].items()
    ):

        if not isinstance(
            skill_id,
            str,
        ):
            raise ValueError(
                "Skill IDs must be strings."
            )

        if not isinstance(
            entry,
            dict,
        ):
            raise ValueError(
                f"Invalid entry for "
                f"skill '{skill_id}'."
            )

        if "level" not in entry:
            raise ValueError(
                f"Skill '{skill_id}' "
                "is missing level."
            )

        if "evidence" not in entry:
            raise ValueError(
                f"Skill '{skill_id}' "
                "is missing evidence."
            )

        if "evidence_strength" not in entry:
            raise ValueError(
                f"Skill '{skill_id}' "
                "is missing evidence_strength."
            )

        normalize_skill_level(
            entry["level"]
        )

        normalize_evidence_strength(
            entry["evidence_strength"]
        )

        if not isinstance(
            entry["evidence"],
            list,
        ):
            raise ValueError(
                f"Evidence for '{skill_id}' "
                "must be a list."
            )

    return True


# ============================================================
# PROFILE SUMMARY
# ============================================================

def get_skill_profile_summary(
    profile,
):
    """
    Return useful summary information about the profile.
    """

    validate_student_skill_profile(
        profile
    )

    skills = profile[
        "skills"
    ]

    total = len(skills)

    known = 0
    unknown = 0

    by_level = {
        "none": 0,
        "foundational": 0,
        "beginner": 0,
        "intermediate": 0,
        "advanced": 0,
    }

    for entry in skills.values():

        level = entry[
            "level"
        ]

        if level == "unknown":

            unknown += 1

        else:

            known += 1

            by_level[
                level
            ] += 1

    if total > 0:

        evidence_coverage = (
            known
            / total
        ) * 100

    else:

        evidence_coverage = 0.0

    return {
        "student_mode": profile[
            "student_mode"
        ],

        "total_skills": total,

        "known_skills": known,

        "unknown_skills": unknown,

        "evidence_coverage": round(
            evidence_coverage,
            2,
        ),

        "by_level": by_level,
    }


# ============================================================
# PRINT PROFILE
# ============================================================

def print_student_skill_profile(
    profile,
):
    """
    Print a readable student skill profile.
    """

    validate_student_skill_profile(
        profile
    )

    summary = get_skill_profile_summary(
        profile
    )

    print()

    print(
        "=" * 80
    )

    print(
        "STUDENT SKILL PROFILE"
    )

    print(
        "=" * 80
    )

    print(
        f"Mode: "
        f"{summary['student_mode']}"
    )

    print(
        f"Skill evidence coverage: "
        f"{summary['evidence_coverage']:.1f}%"
    )

    print()

    if not profile["skills"]:

        print(
            "No skills have been provided yet."
        )

        return

    for skill_id, entry in (
        profile["skills"].items()
    ):

        display_name = (
            format_skill_name(
                skill_id
            )
        )

        level = (
            SKILL_LEVEL_DISPLAY_NAMES[
                entry["level"]
            ]
        )

        evidence_strength = (
            entry[
                "evidence_strength"
            ]
        )

        print(
            f"{display_name}: "
            f"{level}"
        )

        print(
            f"  Evidence strength: "
            f"{evidence_strength}"
        )

        if entry["evidence"]:

            print(
                "  Evidence:"
            )

            for evidence_item in (
                entry["evidence"]
            ):

                print(
                    f"    - "
                    f"{evidence_item}"
                )

        else:

            print(
                "  Evidence: "
                "Self-reported"
            )

        print()


# ============================================================
# TEST PROFILE — COLLEGE STUDENT
# ============================================================

COLLEGE_TEST_PROFILE = {

    "python": {
        "level": "beginner",

        "evidence": [
            "Completed Python fundamentals"
        ],

        "evidence_strength": "supported",
    },

    "sql": {
        "level": "foundational",

        "evidence": [
            "Practiced basic SQL queries"
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

    "programming": {
        "level": "intermediate",

        "evidence": [
            "Regular programming practice",
            "Completed academic programming projects"
        ],

        "evidence_strength": "strong",
    },

    "communication": {
        "level": "beginner",

        "evidence": [],

        "evidence_strength": "self_reported",
    },

    "machine_learning": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },
}


# ============================================================
# TEST PROFILE — SCHOOL STUDENT
# ============================================================

SCHOOL_TEST_PROFILE = {

    "problem_solving": {
        "level": "intermediate",

        "evidence": [
            "Enjoys solving logic-based problems"
        ],

        "evidence_strength": "supported",
    },

    "mathematics": {
        "level": "beginner",

        "evidence": [
            "Currently studying mathematics"
        ],

        "evidence_strength": "supported",
    },

    "digital_tools": {
        "level": "foundational",

        "evidence": [
            "Regularly uses digital learning tools"
        ],

        "evidence_strength": "supported",
    },

    "communication": {
        "level": "unknown",

        "evidence": [],

        "evidence_strength": "self_reported",
    },
}


# ============================================================
# MAIN TEST
# ============================================================

if __name__ == "__main__":

    print(
        "Student Skill Profile validation"
    )

    print(
        "=" * 80
    )

    # --------------------------------------------------------
    # College profile
    # --------------------------------------------------------

    college_profile = (
        create_student_skill_profile(
            "college",
            COLLEGE_TEST_PROFILE,
        )
    )

    validate_student_skill_profile(
        college_profile
    )

    print_student_skill_profile(
        college_profile
    )

    # --------------------------------------------------------
    # School profile
    # --------------------------------------------------------

    school_profile = (
        create_student_skill_profile(
            "school",
            SCHOOL_TEST_PROFILE,
        )
    )

    validate_student_skill_profile(
        school_profile
    )

    print_student_skill_profile(
        school_profile
    )

    # --------------------------------------------------------
    # Test updating a skill
    # --------------------------------------------------------

    set_student_skill(
        college_profile,
        "machine_learning",
        "beginner",
        evidence=[
            "Completed an introductory ML course"
        ],
        evidence_strength="supported",
    )

    validate_student_skill_profile(
        college_profile
    )

    print(
        "Skill update test successful."
    )

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    college_summary = (
        get_skill_profile_summary(
            college_profile
        )
    )

    school_summary = (
        get_skill_profile_summary(
            school_profile
        )
    )

    print()

    print(
        "=" * 80
    )

    print(
        "Student skill profile validation successful."
    )

    print(
        f"College profile skills: "
        f"{college_summary['total_skills']}"
    )

    print(
        f"School profile skills: "
        f"{school_summary['total_skills']}"
    )

    print(
        "Unknown and known skill states are handled separately."
    )