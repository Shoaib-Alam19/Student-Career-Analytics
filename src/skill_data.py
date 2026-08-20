"""
Career Skill Knowledge Base
---------------------------

Contains structured skill requirements for the careers
currently supported by Student Career Navigator.

This is a knowledge-based layer.

It is NOT an ML model and it does NOT determine whether
a student is eligible for a career.

Each skill contains:

    - category
    - importance
    - expected_level

Importance:
    core       -> essential / highly important
    important  -> strongly useful
    supporting -> useful but less central

Expected level:
    foundational
    beginner
    intermediate
    advanced
"""


# ============================================================
# LEVEL ORDER
# ============================================================

SKILL_LEVELS = {
    "none": 0,
    "foundational": 1,
    "beginner": 2,
    "intermediate": 3,
    "advanced": 4,
}


# ============================================================
# IMPORTANCE ORDER
# ============================================================

SKILL_IMPORTANCE = {
    "core": 3,
    "important": 2,
    "supporting": 1,
}


# ============================================================
# CAREER SKILL PROFILES
# ============================================================

CAREER_SKILLS = {

    # ========================================================
    # SOFTWARE DEVELOPER
    # ========================================================

    "software_developer": {

        "career_name": "Software Developer",

        "skills": {

            "programming": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "data_structures_algorithms": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "problem_solving": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "object_oriented_programming": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "databases_sql": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "version_control": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "beginner",
            },

            "software_development": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "debugging": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "communication": {
                "category": "Professional",
                "importance": "supporting",
                "expected_level": "intermediate",
            },

            "teamwork": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "intermediate",
            },
        },
    },


    # ========================================================
    # DATA ANALYST
    # ========================================================

    "data_analyst": {

        "career_name": "Data Analyst",

        "skills": {

            "excel_spreadsheets": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "statistics": {
                "category": "Analytical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "sql": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "data_cleaning": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "data_visualization": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "python": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "beginner",
            },

            "analytical_thinking": {
                "category": "Analytical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "business_understanding": {
                "category": "Domain",
                "importance": "important",
                "expected_level": "beginner",
            },

            "communication": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "presentation": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "beginner",
            },
        },
    },


    # ========================================================
    # DATA SCIENTIST
    # ========================================================

    "data_scientist": {

        "career_name": "Data Scientist",

        "skills": {

            "python": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "statistics": {
                "category": "Analytical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "probability": {
                "category": "Analytical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "linear_algebra": {
                "category": "Mathematics",
                "importance": "important",
                "expected_level": "foundational",
            },

            "sql": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "pandas": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "data_visualization": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "machine_learning": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "data_cleaning": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "analytical_thinking": {
                "category": "Analytical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "research": {
                "category": "Analytical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "communication": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "projects": {
                "category": "Experience",
                "importance": "core",
                "expected_level": "intermediate",
            },
        },
    },


    # ========================================================
    # CYBERSECURITY ANALYST
    # ========================================================

    "cybersecurity_analyst": {

        "career_name": "Cybersecurity Analyst",

        "skills": {

            "networking": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "operating_systems": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "cybersecurity_fundamentals": {
                "category": "Security",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "linux": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "beginner",
            },

            "security_monitoring": {
                "category": "Security",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "threat_analysis": {
                "category": "Security",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "problem_solving": {
                "category": "Analytical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "attention_to_detail": {
                "category": "Analytical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "scripting": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "beginner",
            },

            "communication": {
                "category": "Professional",
                "importance": "supporting",
                "expected_level": "beginner",
            },
        },
    },


    # ========================================================
    # UI/UX DESIGNER
    # ========================================================

    "ui_ux_designer": {

        "career_name": "UI/UX Designer",

        "skills": {

            "user_research": {
                "category": "Design",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "wireframing": {
                "category": "Design",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "prototyping": {
                "category": "Design",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "visual_design": {
                "category": "Design",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "design_principles": {
                "category": "Design",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "user_empathy": {
                "category": "People",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "creative_thinking": {
                "category": "Creative",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "communication": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "portfolio_development": {
                "category": "Experience",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "design_tools": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },
        },
    },


    # ========================================================
    # DOCTOR
    # ========================================================

    "doctor": {

        "career_name": "Doctor",

        "skills": {

            "biology": {
                "category": "Academic",
                "importance": "core",
                "expected_level": "advanced",
            },

            "chemistry": {
                "category": "Academic",
                "importance": "core",
                "expected_level": "advanced",
            },

            "anatomy": {
                "category": "Medical",
                "importance": "core",
                "expected_level": "advanced",
            },

            "physiology": {
                "category": "Medical",
                "importance": "core",
                "expected_level": "advanced",
            },

            "clinical_reasoning": {
                "category": "Medical",
                "importance": "core",
                "expected_level": "advanced",
            },

            "patient_communication": {
                "category": "Professional",
                "importance": "core",
                "expected_level": "advanced",
            },

            "attention_to_detail": {
                "category": "Professional",
                "importance": "core",
                "expected_level": "advanced",
            },

            "empathy": {
                "category": "Professional",
                "importance": "core",
                "expected_level": "advanced",
            },

            "decision_making": {
                "category": "Analytical",
                "importance": "important",
                "expected_level": "advanced",
            },

            "stress_management": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "intermediate",
            },
        },
    },


    # ========================================================
    # NURSE
    # ========================================================

    "nurse": {

        "career_name": "Nurse",

        "skills": {

            "biology": {
                "category": "Academic",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "anatomy": {
                "category": "Medical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "patient_care": {
                "category": "Medical",
                "importance": "core",
                "expected_level": "advanced",
            },

            "patient_communication": {
                "category": "Professional",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "empathy": {
                "category": "Professional",
                "importance": "core",
                "expected_level": "advanced",
            },

            "attention_to_detail": {
                "category": "Professional",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "teamwork": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "decision_making": {
                "category": "Analytical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "stress_management": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "clinical_skills": {
                "category": "Medical",
                "importance": "core",
                "expected_level": "intermediate",
            },
        },
    },


    # ========================================================
    # LAWYER
    # ========================================================

    "lawyer": {

        "career_name": "Lawyer",

        "skills": {

            "legal_reasoning": {
                "category": "Legal",
                "importance": "core",
                "expected_level": "advanced",
            },

            "legal_research": {
                "category": "Legal",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "reading_comprehension": {
                "category": "Analytical",
                "importance": "core",
                "expected_level": "advanced",
            },

            "writing": {
                "category": "Communication",
                "importance": "core",
                "expected_level": "advanced",
            },

            "verbal_communication": {
                "category": "Communication",
                "importance": "core",
                "expected_level": "advanced",
            },

            "argumentation": {
                "category": "Legal",
                "importance": "core",
                "expected_level": "advanced",
            },

            "critical_thinking": {
                "category": "Analytical",
                "importance": "core",
                "expected_level": "advanced",
            },

            "attention_to_detail": {
                "category": "Analytical",
                "importance": "important",
                "expected_level": "advanced",
            },

            "current_affairs": {
                "category": "Knowledge",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "negotiation": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "intermediate",
            },
        },
    },

    # ========================================================
    # WEB DEVELOPER
    # ========================================================

    "web_developer": {

        "career_name": "Web Developer",

        "skills": {

            "html": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "css": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "javascript": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "react": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "beginner",
            },

            "git": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "beginner",
            },

            "apis": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "beginner",
            },

            "sql": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "beginner",
            },

            "projects": {
                "category": "Experience",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "problem_solving": {
                "category": "Analytical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "communication": {
                "category": "Professional",
                "importance": "supporting",
                "expected_level": "beginner",
            },

        },
    },

        "business_analyst": {

        "career_name": "Business Analyst",

        "skills": {

            "excel_spreadsheets": {
                "category": "Technical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "sql": {
                "category": "Technical",
                "importance": "important",
                "expected_level": "beginner",
            },

            "analytical_thinking": {
                "category": "Analytical",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "business_understanding": {
                "category": "Business",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "communication": {
                "category": "Professional",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "research": {
                "category": "Analytical",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "presentation": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "beginner",
            },

            "problem_solving": {
                "category": "Analytical",
                "importance": "core",
                "expected_level": "intermediate",
            },
        },
    },


    "teacher": {

        "career_name": "Teacher / Educator",

        "skills": {

            "teaching": {
                "category": "Education",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "lesson_planning": {
                "category": "Education",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "communication": {
                "category": "Professional",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "assessment": {
                "category": "Education",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "empathy": {
                "category": "Professional",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "presentation": {
                "category": "Professional",
                "importance": "important",
                "expected_level": "intermediate",
            },

            "classroom_management": {
                "category": "Education",
                "importance": "core",
                "expected_level": "intermediate",
            },

            "subject_knowledge": {
                "category": "Academic",
                "importance": "core",
                "expected_level": "advanced",
            },
        },
    },
}


# ============================================================
# VALIDATION
# ============================================================

def validate_skill_data():
    """
    Validate the career skill knowledge base.
    """

    if not CAREER_SKILLS:
        raise ValueError(
            "CAREER_SKILLS cannot be empty."
        )

    for career_id, career in CAREER_SKILLS.items():

        if "career_name" not in career:
            raise ValueError(
                f"{career_id} is missing career_name."
            )

        if "skills" not in career:
            raise ValueError(
                f"{career_id} is missing skills."
            )

        if not career["skills"]:
            raise ValueError(
                f"{career_id} has no skills."
            )

        for skill_id, skill in (
            career["skills"].items()
        ):

            required_fields = [
                "category",
                "importance",
                "expected_level",
            ]

            for field in required_fields:

                if field not in skill:
                    raise ValueError(
                        f"{career_id} -> "
                        f"{skill_id} is missing "
                        f"{field}."
                    )

            if (
                skill["importance"]
                not in SKILL_IMPORTANCE
            ):
                raise ValueError(
                    f"Invalid importance "
                    f"'{skill['importance']}' "
                    f"for {career_id} -> "
                    f"{skill_id}."
                )

            if (
                skill["expected_level"]
                not in SKILL_LEVELS
            ):
                raise ValueError(
                    f"Invalid level "
                    f"'{skill['expected_level']}' "
                    f"for {career_id} -> "
                    f"{skill_id}."
                )

    return True


# ============================================================
# SUMMARY
# ============================================================

def print_skill_data_summary():
    """
    Print a simple summary of the knowledge base.
    """

    print(
        "Career skill knowledge base validation successful."
    )

    print()

    print(
        f"Number of careers: "
        f"{len(CAREER_SKILLS)}"
    )

    print()

    for career_id, career in (
        CAREER_SKILLS.items()
    ):

        print(
            f"- {career['career_name']}: "
            f"{len(career['skills'])} skills"
        )


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    validate_skill_data()

    print_skill_data_summary()