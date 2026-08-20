"""
Roadmap Personalization Engine
------------------------------

Converts:

    Career roadmap
        +
    Student skill profile
        +
    Skill-gap information

into a personalized learning roadmap.

The engine distinguishes between:

    complete
        The student appears ready to move beyond the stage.

    develop
        The student has some foundation but should strengthen it.

    start
        The student should begin building this area.

    explore
        There is not enough information about the relevant skills.

The engine also respects roadmap prerequisites so that advanced
stages are not presented as immediate priorities when earlier
foundational stages are still incomplete.

This module provides guidance.
It does NOT decide a student's career.
"""


# ============================================================
# IMPORTS
# ============================================================

from roadmap_data import (
    get_roadmap,
    validate_roadmap_data,
)

from skill_gap import (
    calculate_skill_gap,
)

from student_skills import (
    create_student_skill_profile,
    validate_student_skill_profile,
)


# ============================================================
# STATUS CONSTANTS
# ============================================================

STATUS_COMPLETE = "complete"
STATUS_DEVELOP = "develop"
STATUS_START = "start"
STATUS_EXPLORE = "explore"


STATUS_LABELS = {

    STATUS_COMPLETE:
        "Ready to move forward",

    STATUS_DEVELOP:
        "Develop further",

    STATUS_START:
        "Start building",

    STATUS_EXPLORE:
        "Explore first",
}


# ============================================================
# PRIORITY CONSTANTS
# ============================================================

PRIORITY_HIGH = "high"
PRIORITY_MEDIUM = "medium"
PRIORITY_LOW = "low"


# ============================================================
# STUDENT SKILL LEVEL VALUES
# ============================================================

STUDENT_LEVEL_VALUES = {

    "unknown": -1,

    "none": 0,

    "foundational": 1,

    "beginner": 2,

    "intermediate": 3,

    "advanced": 4,
}


# ============================================================
# HELPER — FORMAT SKILL NAME
# ============================================================

def format_skill_name(
    skill_id,
):
    """
    Convert an internal skill ID into readable text.
    """

    return (
        skill_id
        .replace("_", " ")
        .strip()
        .title()
    )


# ============================================================
# HELPER — GET STUDENT SKILL
# ============================================================

def get_student_skill(
    student_profile,
    skill_id,
):
    """
    Return a student's entry for a particular skill.

    Unknown skills are represented explicitly instead of
    being treated as weaknesses.
    """

    skills = student_profile.get(
        "skills",
        {},
    )

    entry = skills.get(
        skill_id
    )

    if entry is None:

        return {
            "level": "unknown",
            "evidence": [],
            "evidence_strength": None,
        }

    return entry


# ============================================================
# HELPER — NORMALIZE LEVEL
# ============================================================

def normalize_level(
    level,
):
    """
    Normalize a skill level.
    """

    if not isinstance(
        level,
        str,
    ):

        return "unknown"

    level = level.strip().lower()

    if level not in STUDENT_LEVEL_VALUES:

        return "unknown"

    return level


# ============================================================
# HELPER — LEVEL VALUE
# ============================================================

def get_level_value(
    level,
):
    """
    Convert a normalized level into a numerical value.
    """

    level = normalize_level(
        level
    )

    return STUDENT_LEVEL_VALUES[
        level
    ]


# ============================================================
# ANALYZE STAGE SKILLS
# ============================================================

def analyze_stage_skills(
    stage,
    student_profile,
):
    """
    Analyze all skills associated with one roadmap stage.
    """

    results = []

    for skill_id in stage[
        "skills"
    ]:

        entry = get_student_skill(
            student_profile,
            skill_id,
        )

        level = normalize_level(
            entry.get(
                "level",
                "unknown",
            )
        )

        results.append(
            {
                "skill_id": skill_id,

                "current_level": level,

                "current_value": (
                    get_level_value(level)
                ),

                "evidence": entry.get(
                    "evidence",
                    [],
                ),

                "evidence_strength": entry.get(
                    "evidence_strength"
                ),
            }
        )

    return results


# ============================================================
# DETERMINE STAGE STATUS
# ============================================================

def determine_stage_status(
    stage_skill_results,
):
    """
    Determine the student's current status for a stage.

    Rules:

        complete
            Every relevant skill is intermediate or advanced.

        develop
            The student has some useful foundation.

        start
            The student has explicit low-level experience.

        explore
            All relevant information is unknown.

    Unknown is never automatically treated as failure.
    """

    if not stage_skill_results:

        return STATUS_EXPLORE

    known = [
        item
        for item in stage_skill_results
        if item["current_level"]
        != "unknown"
    ]

    if not known:

        return STATUS_EXPLORE

    values = [
        item["current_value"]
        for item in known
    ]

    minimum_value = min(
        values
    )

    unknown_count = (
        len(stage_skill_results)
        - len(known)
    )

    # --------------------------------------------------------
    # All skills known and intermediate+
    # --------------------------------------------------------

    if (
        minimum_value >= 3
        and unknown_count == 0
    ):

        return STATUS_COMPLETE

    # --------------------------------------------------------
    # Some foundation exists
    # --------------------------------------------------------

    if minimum_value >= 2:

        return STATUS_DEVELOP

    # --------------------------------------------------------
    # Foundational / none
    # --------------------------------------------------------

    return STATUS_START


# ============================================================
# BUILD STAGE RESULT
# ============================================================

def build_stage_result(
    stage,
    student_profile,
    stage_index,
):
    """
    Build the raw personalized result for one stage.
    """

    skill_analysis = analyze_stage_skills(
        stage,
        student_profile,
    )

    status = determine_stage_status(
        skill_analysis
    )

    return {

        "stage_id": stage[
            "stage_id"
        ],

        "title": stage[
            "title"
        ],

        "purpose": stage[
            "purpose"
        ],

        "skills": stage[
            "skills"
        ],

        "prerequisites": stage[
            "prerequisites"
        ],

        "practice": stage[
            "practice"
        ],

        "project": stage[
            "project"
        ],

        "stage_index": stage_index,

        "status": status,

        "status_label": STATUS_LABELS[
            status
        ],

        "skill_analysis": skill_analysis,

        "prerequisites_complete": False,

        "available_now": False,

        "priority": PRIORITY_LOW,

        "summary": "",
    }


# ============================================================
# CHECK PREREQUISITES
# ============================================================

def check_stage_prerequisites(
    stage_result,
    stage_results_by_id,
):
    """
    Check whether every prerequisite stage is complete.
    """

    prerequisites = stage_result[
        "prerequisites"
    ]

    if not prerequisites:

        return True

    for prerequisite_id in prerequisites:

        prerequisite = (
            stage_results_by_id.get(
                prerequisite_id
            )
        )

        if prerequisite is None:

            return False

        if prerequisite[
            "status"
        ] != STATUS_COMPLETE:

            return False

    return True


# ============================================================
# DETERMINE AVAILABILITY
# ============================================================

def determine_stage_availability(
    stage_result,
    stage_results_by_id,
):
    """
    Determine whether a stage is currently available.

    A stage is available when all its prerequisites
    are complete.

    This is the key mechanism preventing the roadmap
    from pushing advanced learning too early.
    """

    prerequisites_complete = (
        check_stage_prerequisites(
            stage_result,
            stage_results_by_id,
        )
    )

    stage_result[
        "prerequisites_complete"
    ] = prerequisites_complete

    if prerequisites_complete:

        stage_result[
            "available_now"
        ] = True

    else:

        stage_result[
            "available_now"
        ] = False

    return stage_result


# ============================================================
# DETERMINE PRIORITY
# ============================================================

def determine_stage_priority(
    stage_result,
):
    """
    Determine priority after prerequisite availability
    has been calculated.

    Rules:

        Complete
            Low

        Available + Start
            High

        Available + Develop
            High/Medium

        Available + Explore
            Medium

        Not available
            Low

    This means a later stage cannot become an immediate
    priority while its prerequisites are unfinished.
    """

    status = stage_result[
        "status"
    ]

    available = stage_result[
        "available_now"
    ]

    # --------------------------------------------------------
    # Completed
    # --------------------------------------------------------

    if status == STATUS_COMPLETE:

        return PRIORITY_LOW

    # --------------------------------------------------------
    # Blocked by prerequisites
    # --------------------------------------------------------

    if not available:

        return PRIORITY_LOW

    # --------------------------------------------------------
    # Available stages
    # --------------------------------------------------------

    if status == STATUS_START:

        return PRIORITY_HIGH

    if status == STATUS_DEVELOP:

        return PRIORITY_HIGH

    if status == STATUS_EXPLORE:

        return PRIORITY_MEDIUM

    return PRIORITY_LOW


# ============================================================
# GENERATE STAGE SUMMARY
# ============================================================

def generate_stage_summary(
    stage_result,
):
    """
    Generate a student-friendly explanation.
    """

    title = stage_result[
        "title"
    ]

    status = stage_result[
        "status"
    ]

    available = stage_result[
        "available_now"
    ]

    # --------------------------------------------------------
    # Complete
    # --------------------------------------------------------

    if status == STATUS_COMPLETE:

        return (
            f"You appear to have enough foundation "
            f"to move beyond {title}."
        )

    # --------------------------------------------------------
    # Blocked
    # --------------------------------------------------------

    if not available:

        return (
            f"{title} is part of your longer-term path, "
            f"but its prerequisite stages should be developed "
            f"first."
        )

    # --------------------------------------------------------
    # Develop
    # --------------------------------------------------------

    if status == STATUS_DEVELOP:

        return (
            f"You already have some foundation for "
            f"{title}. Strengthen it before moving ahead."
        )

    # --------------------------------------------------------
    # Start
    # --------------------------------------------------------

    if status == STATUS_START:

        return (
            f"{title} should be one of your current "
            f"learning priorities."
        )

    # --------------------------------------------------------
    # Explore
    # --------------------------------------------------------

    return (
        f"We need more information about your current "
        f"skills before making a strong recommendation "
        f"about {title}."
    )


# ============================================================
# FINALIZE STAGE RESULTS
# ============================================================

def finalize_stage_results(
    stage_results,
):
    """
    Apply prerequisite logic, priority, and summaries
    to every stage.
    """

    stage_results_by_id = {
        stage["stage_id"]: stage
        for stage in stage_results
    }

    for stage in stage_results:

        determine_stage_availability(
            stage,
            stage_results_by_id,
        )

    for stage in stage_results:

        stage[
            "priority"
        ] = determine_stage_priority(
            stage
        )

        stage[
            "summary"
        ] = generate_stage_summary(
            stage
        )

    return stage_results


# ============================================================
# FIND CURRENT STAGE
# ============================================================

def determine_starting_stage(
    stage_results,
):
    """
    Find the FIRST stage that should be actively worked on.

    Ordering preference:

        1. Available start
        2. Available develop
        3. Available explore

    Completed and prerequisite-blocked stages are skipped.
    """

    # --------------------------------------------------------
    # Available start
    # --------------------------------------------------------

    for stage in stage_results:

        if (
            stage["available_now"]
            and stage["status"]
            == STATUS_START
        ):

            return stage

    # --------------------------------------------------------
    # Available develop
    # --------------------------------------------------------

    for stage in stage_results:

        if (
            stage["available_now"]
            and stage["status"]
            == STATUS_DEVELOP
        ):

            return stage

    # --------------------------------------------------------
    # Available explore
    # --------------------------------------------------------

    for stage in stage_results:

        if (
            stage["available_now"]
            and stage["status"]
            == STATUS_EXPLORE
        ):

            return stage

    return None


# ============================================================
# FIND NEXT STAGE
# ============================================================

def determine_next_stage(
    stage_results,
    current_stage,
):
    """
    Find the next meaningful stage after the current stage.

    A stage must not be presented as the next stage if
    its prerequisites are not satisfied.
    """

    if current_stage is None:

        return None

    current_index = current_stage[
        "stage_index"
    ]

    # --------------------------------------------------------
    # First look forward for an available incomplete stage
    # --------------------------------------------------------

    for stage in stage_results[
        current_index + 1:
    ]:

        if (
            stage["available_now"]
            and stage["status"]
            != STATUS_COMPLETE
        ):

            return stage

    # --------------------------------------------------------
    # If no available later stage exists, return the next
    # blocked stage as a longer-term direction.
    # --------------------------------------------------------

    for stage in stage_results[
        current_index + 1:
    ]:

        if stage[
            "status"
        ] != STATUS_COMPLETE:

            return stage

    return None


# ============================================================
# BUILD IMMEDIATE ACTIONS
# ============================================================

def build_immediate_actions(
    stage_results,
    starting_stage,
    next_stage,
):
    """
    Build a SHORT action plan.

    Unlike the previous version, this does not dump every
    incomplete stage into the immediate action plan.

    The student gets:

        1. Current focus
        2. Next focus

    Longer-term stages remain visible in the roadmap.
    """

    actions = []

    if starting_stage is not None:

        first_action = (
            starting_stage["practice"][0]
            if starting_stage["practice"]
            else starting_stage["purpose"]
        )

        actions.append(
            {
                "type": "current",

                "stage_id": starting_stage[
                    "stage_id"
                ],

                "title": starting_stage[
                    "title"
                ],

                "priority": PRIORITY_HIGH,

                "action": first_action,

                "project": starting_stage[
                    "project"
                ],
            }
        )

    if (
        next_stage is not None
        and (
            starting_stage is None
            or next_stage["stage_id"]
            != starting_stage["stage_id"]
        )
    ):

        next_action = (
            next_stage["practice"][0]
            if next_stage["practice"]
            else next_stage["purpose"]
        )

        actions.append(
            {
                "type": "next",

                "stage_id": next_stage[
                    "stage_id"
                ],

                "title": next_stage[
                    "title"
                ],

                "priority": PRIORITY_MEDIUM,

                "action": next_action,

                "project": next_stage[
                    "project"
                ],
            }
        )

    return actions


# ============================================================
# LONG-TERM STAGES
# ============================================================

def build_later_stages(
    stage_results,
    starting_stage,
    next_stage,
):
    """
    Return incomplete stages that are not immediate actions.

    These are shown as the student's longer-term path.
    """

    immediate_ids = set()

    if starting_stage is not None:

        immediate_ids.add(
            starting_stage[
                "stage_id"
            ]
        )

    if next_stage is not None:

        immediate_ids.add(
            next_stage[
                "stage_id"
            ]
        )

    later = []

    for stage in stage_results:

        if stage[
            "status"
        ] == STATUS_COMPLETE:

            continue

        if stage[
            "stage_id"
        ] in immediate_ids:

            continue

        later.append(
            stage
        )

    return later


# ============================================================
# GENERATE PERSONALIZED ROADMAP
# ============================================================

def generate_personalized_roadmap(
    career_id,
    student_profile,
):
    """
    Generate a complete personalized roadmap.

    Parameters
    ----------
    career_id:
        Career identifier from roadmap_data.py.

    student_profile:
        Structured student skill profile.

    Returns
    -------
    dict
        Personalized roadmap.
    """

    # --------------------------------------------------------
    # Validate source data
    # --------------------------------------------------------

    validate_roadmap_data()

    validate_student_skill_profile(
        student_profile
    )

    # --------------------------------------------------------
    # Get career roadmap
    # --------------------------------------------------------

    roadmap = get_roadmap(
        career_id
    )

    # --------------------------------------------------------
    # Build raw stage results
    # --------------------------------------------------------

    stage_results = []

    for index, stage in enumerate(
        roadmap["stages"]
    ):

        stage_result = (
            build_stage_result(
                stage,
                student_profile,
                index,
            )
        )

        stage_results.append(
            stage_result
        )

    # --------------------------------------------------------
    # Apply prerequisite logic
    # --------------------------------------------------------

    stage_results = (
        finalize_stage_results(
            stage_results
        )
    )

    # --------------------------------------------------------
    # Current focus
    # --------------------------------------------------------

    starting_stage = (
        determine_starting_stage(
            stage_results
        )
    )

    # --------------------------------------------------------
    # Next focus
    # --------------------------------------------------------

    next_stage = (
        determine_next_stage(
            stage_results,
            starting_stage,
        )
    )

    # --------------------------------------------------------
    # Immediate actions
    # --------------------------------------------------------

    immediate_actions = (
        build_immediate_actions(
            stage_results,
            starting_stage,
            next_stage,
        )
    )

    # --------------------------------------------------------
    # Longer-term path
    # --------------------------------------------------------

    later_stages = (
        build_later_stages(
            stage_results,
            starting_stage,
            next_stage,
        )
    )

    # --------------------------------------------------------
    # Skill gap
    # --------------------------------------------------------

    skill_gap_report = (
        calculate_skill_gap(
            career_id,
            student_profile,
        )
    )

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    completed_count = sum(
        1
        for stage in stage_results
        if stage["status"]
        == STATUS_COMPLETE
    )

    develop_count = sum(
        1
        for stage in stage_results
        if stage["status"]
        == STATUS_DEVELOP
    )

    start_count = sum(
        1
        for stage in stage_results
        if stage["status"]
        == STATUS_START
    )

    explore_count = sum(
        1
        for stage in stage_results
        if stage["status"]
        == STATUS_EXPLORE
    )

    # --------------------------------------------------------
    # Return
    # --------------------------------------------------------

    return {

        "career_id": career_id,

        "career_name": roadmap[
            "career_name"
        ],

        "domain": roadmap[
            "domain"
        ],

        "description": roadmap[
            "description"
        ],

        "student_mode": student_profile[
            "student_mode"
        ],

        "starting_stage": starting_stage,

        "next_stage": next_stage,

        "stage_results": stage_results,

        "immediate_actions": immediate_actions,

        "later_stages": later_stages,

        "skill_gap": skill_gap_report,

        "statistics": {

            "total_stages": len(
                stage_results
            ),

            "completed": completed_count,

            "develop": develop_count,

            "start": start_count,

            "explore": explore_count,
        },
    }


# ============================================================
# PRINT STAGE
# ============================================================

def print_stage(
    stage,
):
    """
    Print one roadmap stage.
    """

    print()

    print(
        "-" * 70
    )

    print(
        stage["title"]
    )

    print(
        f"Status: "
        f"{stage['status_label']}"
    )

    if stage[
        "available_now"
    ]:

        print(
            "Availability: Available now"
        )

    else:

        print(
            "Availability: Later "
            "(prerequisites incomplete)"
        )

    print(
        f"Priority: "
        f"{stage['priority'].title()}"
    )

    print()

    print(
        "Why:"
    )

    print(
        f"  {stage['purpose']}"
    )

    print()

    print(
        "Relevant skills:"
    )

    for skill in stage[
        "skill_analysis"
    ]:

        print(
            f"  - "
            f"{format_skill_name(skill['skill_id'])}: "
            f"{skill['current_level']}"
        )

    if stage[
        "prerequisites"
    ]:

        print()

        print(
            "Prerequisites:"
        )

        for prerequisite in stage[
            "prerequisites"
        ]:

            print(
                f"  - "
                f"{format_skill_name(prerequisite)}"
            )

    print()

    print(
        "What to practice:"
    )

    for practice in stage[
        "practice"
    ]:

        print(
            f"  - {practice}"
        )

    print()

    print(
        "Suggested project:"
    )

    print(
        f"  {stage['project']}"
    )


# ============================================================
# PRINT ROADMAP
# ============================================================

def print_roadmap(
    roadmap,
):
    """
    Print a student-friendly personalized roadmap.
    """

    print()

    print(
        "=" * 80
    )

    print(
        roadmap["career_name"]
    )

    print(
        "=" * 80
    )

    print(
        f"Domain: "
        f"{roadmap['domain']}"
    )

    print(
        f"Student mode: "
        f"{roadmap['student_mode']}"
    )

    print()

    print(
        roadmap["description"]
    )

    # ========================================================
    # START NOW
    # ========================================================

    print()

    print(
        "🎯 START NOW"
    )

    print(
        "-" * 70
    )

    starting_stage = roadmap[
        "starting_stage"
    ]

    if starting_stage is None:

        print(
            "No incomplete starting stage was identified."
        )

    else:

        print(
            starting_stage["title"]
        )

        print(
            starting_stage["summary"]
        )

        print()

        print(
            "First action:"
        )

        if starting_stage[
            "practice"
        ]:

            print(
                f"  - "
                f"{starting_stage['practice'][0]}"
            )

        print()

        print(
            "Suggested project:"
        )

        print(
            f"  {starting_stage['project']}"
        )

    # ========================================================
    # NEXT
    # ========================================================

    print()

    print(
        "➡️ NEXT"
    )

    print(
        "-" * 70
    )

    next_stage = roadmap[
        "next_stage"
    ]

    if next_stage is None:

        print(
            "No additional stage currently identified."
        )

    else:

        print(
            next_stage["title"]
        )

        print(
            next_stage["summary"]
        )

    # ========================================================
    # LATER
    # ========================================================

    print()

    print(
        "🔭 LATER"
    )

    print(
        "-" * 70
    )

    later_stages = roadmap[
        "later_stages"
    ]

    if not later_stages:

        print(
            "No additional incomplete stages."
        )

    else:

        for stage in later_stages:

            availability = (
                "available"
                if stage["available_now"]
                else "after prerequisites"
            )

            print(
                f"  - "
                f"{stage['title']} "
                f"({availability})"
            )

    # ========================================================
    # COMPLETE ROADMAP
    # ========================================================

    print()

    print(
        "=" * 80
    )

    print(
        "FULL PERSONALIZED ROADMAP"
    )

    print(
        "=" * 80
    )

    for stage in roadmap[
        "stage_results"
    ]:

        print_stage(
            stage
        )

    # ========================================================
    # IMMEDIATE ACTION PLAN
    # ========================================================

    print()

    print(
        "=" * 80
    )

    print(
        "IMMEDIATE ACTION PLAN"
    )

    print(
        "=" * 80
    )

    actions = roadmap[
        "immediate_actions"
    ]

    if not actions:

        print(
            "No immediate development action identified."
        )

    else:

        for index, action in enumerate(
            actions,
            start=1,
        ):

            label = (
                "CURRENT"
                if action["type"]
                == "current"
                else "NEXT"
            )

            print()

            print(
                f"{index}. "
                f"[{label}] "
                f"{action['title']}"
            )

            print(
                f"   Action: "
                f"{action['action']}"
            )

            print(
                f"   Project: "
                f"{action['project']}"
            )

    # ========================================================
    # STATUS
    # ========================================================

    stats = roadmap[
        "statistics"
    ]

    print()

    print(
        "=" * 80
    )

    print(
        "ROADMAP STATUS"
    )

    print(
        "=" * 80
    )

    print(
        f"Completed stages: "
        f"{stats['completed']}"
    )

    print(
        f"Stages needing development: "
        f"{stats['develop']}"
    )

    print(
        f"Stages to start: "
        f"{stats['start']}"
    )

    print(
        f"Stages needing more information: "
        f"{stats['explore']}"
    )


# ============================================================
# TEST STUDENTS
# ============================================================

def build_test_student_profiles():
    """
    Build the same test students used by the Skill-Gap Engine.
    """

    from skill_gap import (
        STUDENT_A_SKILLS,
        STUDENT_B_SKILLS,
    )

    student_a = (
        create_student_skill_profile(
            "college",
            STUDENT_A_SKILLS,
        )
    )

    student_b = (
        create_student_skill_profile(
            "school",
            STUDENT_B_SKILLS,
        )
    )

    return (
        student_a,
        student_b,
    )


# ============================================================
# VALIDATION
# ============================================================

def validate_roadmap_engine():
    """
    Validate the complete roadmap engine.
    """

    validate_roadmap_data()

    student_a, student_b = (
        build_test_student_profiles()
    )

    validate_student_skill_profile(
        student_a
    )

    validate_student_skill_profile(
        student_b
    )

    # --------------------------------------------------------
    # Student A
    # --------------------------------------------------------

    roadmap_a = (
        generate_personalized_roadmap(
            "data_scientist",
            student_a,
        )
    )

    if not roadmap_a[
        "stage_results"
    ]:

        raise ValueError(
            "Student A roadmap was not generated."
        )

    # --------------------------------------------------------
    # Student B
    # --------------------------------------------------------

    roadmap_b = (
        generate_personalized_roadmap(
            "nurse",
            student_b,
        )
    )

    if not roadmap_b[
        "stage_results"
    ]:

        raise ValueError(
            "Student B roadmap was not generated."
        )

    # --------------------------------------------------------
    # Validate statuses
    # --------------------------------------------------------

    valid_statuses = {
        STATUS_COMPLETE,
        STATUS_DEVELOP,
        STATUS_START,
        STATUS_EXPLORE,
    }

    for roadmap in (
        roadmap_a,
        roadmap_b,
    ):

        for stage in roadmap[
            "stage_results"
        ]:

            if stage[
                "status"
            ] not in valid_statuses:

                raise ValueError(
                    f"Invalid roadmap status: "
                    f"{stage['status']}"
                )

    return True


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    validate_roadmap_engine()

    print(
        "Roadmap personalization engine validation successful."
    )

    # ========================================================
    # STUDENT A
    # ========================================================

    student_a, student_b = (
        build_test_student_profiles()
    )

    roadmap_a = (
        generate_personalized_roadmap(
            "data_scientist",
            student_a,
        )
    )

    print()

    print(
        "STUDENT A — DATA SCIENTIST"
    )

    print_roadmap(
        roadmap_a
    )

    # ========================================================
    # STUDENT B
    # ========================================================

    roadmap_b = (
        generate_personalized_roadmap(
            "nurse",
            student_b,
        )
    )

    print()

    print(
        "STUDENT B — NURSE"
    )

    print_roadmap(
        roadmap_b
    )

    # ========================================================
    # FINAL STATUS
    # ========================================================

    print()

    print(
        "=" * 80
    )

    print(
        "Roadmap personalization test completed successfully."
    )

    print(
        "Prerequisites are now used when determining "
        "roadmap availability."
    )

    print(
        "Unknown skills are not automatically treated "
        "as weaknesses."
    )