"""
Career Profile Knowledge Base
-----------------------------

Defines structured career profiles used by the
Student Career Navigator.

IMPORTANT:
    Requirement scores represent the RELEVANCE of a
    dimension to a career.

They do NOT represent:
    - minimum eligibility
    - probability of success
    - intelligence requirements
    - a student's suitability by themselves

Scale:
    0  = not particularly relevant
    5  = moderately relevant
    8  = highly relevant
    10 = extremely relevant


Current career domains:
    - Technology & Computing
    - Medicine & Healthcare
    - Law & Justice
    - Design & Creative

Current careers:
    - Software Developer
    - Doctor
    - Lawyer
    - Data Analyst
    - Data Scientist
    - Cybersecurity Analyst
    - UI/UX Designer
    - Nurse
"""


# ============================================================
# 1. CAREER PROFILES
# ============================================================

CAREER_PROFILES = {

    # ========================================================
    # TECHNOLOGY & COMPUTING
    # ========================================================

    "software_developer": {

        "name": "Software Developer",

        "domain": "Technology & Computing",

        "description": (
            "Designs, builds, tests, and maintains software "
            "applications and systems."
        ),

        "education_notes": (
            "Common pathways include Computer Science, "
            "Information Technology, Software Engineering, "
            "or related technical education. "
            "Skills and demonstrated ability are also important."
        ),

        "interest_requirements": {

            "technology": 10.0,
            "mathematics": 7.0,
            "science": 4.0,
            "biology_health": 0.0,
            "business": 3.0,
            "finance": 2.0,
            "law": 0.0,
            "social_issues": 2.0,
            "public_service": 1.0,
            "communication": 4.0,
            "creative_arts": 4.0,
            "media": 2.0,
            "people_helping": 2.0,
            "research": 6.0,
            "nature_environment": 1.0,
            "physical_activity": 1.0,
        },

        "aptitude_requirements": {

            "logical_reasoning": 9.0,
            "numerical_ability": 6.0,
            "analytical_thinking": 9.0,
            "problem_solving": 10.0,
            "verbal_ability": 5.0,
            "spatial_reasoning": 4.0,
            "creative_thinking": 6.0,
            "attention_detail": 8.0,
        },

        "work_style_requirements": {

            "people_interaction": 4.0,
            "helping_others": 3.0,
            "teamwork": 6.0,
            "independent_work": 8.0,
            "leadership": 4.0,
            "data_work": 6.0,
            "technology_work": 10.0,
            "creative_work": 6.0,
            "research_work": 6.0,
            "field_work": 2.0,
            "structured_work": 7.0,
            "flexible_work": 6.0,
        },

        "core_skills": [
            "Programming",
            "Data Structures and Algorithms",
            "Object-Oriented Programming",
            "Database Fundamentals",
            "Software Development",
            "Version Control",
            "Debugging",
            "Problem Solving",
        ],
    },


    "data_analyst": {

        "name": "Data Analyst",

        "domain": "Technology & Computing",

        "description": (
            "Collects, cleans, analyzes, and communicates "
            "insights from data to support decisions."
        ),

        "education_notes": (
            "Relevant pathways include Computer Science, "
            "Data Science, Statistics, Mathematics, Economics, "
            "Business, or related fields."
        ),

        "interest_requirements": {

            "technology": 8.0,
            "mathematics": 8.0,
            "science": 4.0,
            "biology_health": 1.0,
            "business": 7.0,
            "finance": 5.0,
            "law": 0.0,
            "social_issues": 3.0,
            "public_service": 2.0,
            "communication": 6.0,
            "creative_arts": 3.0,
            "media": 3.0,
            "people_helping": 3.0,
            "research": 7.0,
            "nature_environment": 2.0,
            "physical_activity": 1.0,
        },

        "aptitude_requirements": {

            "logical_reasoning": 7.0,
            "numerical_ability": 9.0,
            "analytical_thinking": 10.0,
            "problem_solving": 8.0,
            "verbal_ability": 6.0,
            "spatial_reasoning": 3.0,
            "creative_thinking": 5.0,
            "attention_detail": 9.0,
        },

        "work_style_requirements": {

            "people_interaction": 5.0,
            "helping_others": 3.0,
            "teamwork": 6.0,
            "independent_work": 7.0,
            "leadership": 3.0,
            "data_work": 10.0,
            "technology_work": 8.0,
            "creative_work": 4.0,
            "research_work": 8.0,
            "field_work": 2.0,
            "structured_work": 8.0,
            "flexible_work": 5.0,
        },

        "core_skills": [
            "Excel",
            "SQL",
            "Statistics",
            "Data Cleaning",
            "Python",
            "Pandas",
            "Data Visualization",
            "Business Communication",
        ],
    },


    "data_scientist": {

        "name": "Data Scientist",

        "domain": "Technology & Computing",

        "description": (
            "Uses statistics, programming, data analysis, "
            "and machine learning to solve complex problems."
        ),

        "education_notes": (
            "Common pathways include Computer Science, "
            "Data Science, Statistics, Mathematics, "
            "Engineering, or related quantitative fields."
        ),

        "interest_requirements": {

            "technology": 9.0,
            "mathematics": 10.0,
            "science": 7.0,
            "biology_health": 2.0,
            "business": 5.0,
            "finance": 4.0,
            "law": 0.0,
            "social_issues": 2.0,
            "public_service": 1.0,
            "communication": 4.0,
            "creative_arts": 3.0,
            "media": 1.0,
            "people_helping": 2.0,
            "research": 10.0,
            "nature_environment": 2.0,
            "physical_activity": 1.0,
        },

        "aptitude_requirements": {

            "logical_reasoning": 9.0,
            "numerical_ability": 10.0,
            "analytical_thinking": 10.0,
            "problem_solving": 10.0,
            "verbal_ability": 5.0,
            "spatial_reasoning": 4.0,
            "creative_thinking": 6.0,
            "attention_detail": 9.0,
        },

        "work_style_requirements": {

            "people_interaction": 3.0,
            "helping_others": 2.0,
            "teamwork": 5.0,
            "independent_work": 8.0,
            "leadership": 3.0,
            "data_work": 10.0,
            "technology_work": 9.0,
            "creative_work": 5.0,
            "research_work": 10.0,
            "field_work": 1.0,
            "structured_work": 7.0,
            "flexible_work": 6.0,
        },

        "core_skills": [
            "Python",
            "Statistics",
            "Probability",
            "SQL",
            "Pandas",
            "NumPy",
            "Data Visualization",
            "Machine Learning",
            "Model Evaluation",
        ],
    },


    "cybersecurity_analyst": {

        "name": "Cybersecurity Analyst",

        "domain": "Technology & Computing",

        "description": (
            "Protects computer systems, networks, and data "
            "from security threats and investigates incidents."
        ),

        "education_notes": (
            "Common pathways include Computer Science, "
            "Cybersecurity, Information Technology, "
            "or related technical education."
        ),

        "interest_requirements": {

            "technology": 10.0,
            "mathematics": 6.0,
            "science": 4.0,
            "biology_health": 0.0,
            "business": 3.0,
            "finance": 3.0,
            "law": 4.0,
            "social_issues": 2.0,
            "public_service": 3.0,
            "communication": 4.0,
            "creative_arts": 2.0,
            "media": 1.0,
            "people_helping": 3.0,
            "research": 8.0,
            "nature_environment": 0.0,
            "physical_activity": 2.0,
        },

        "aptitude_requirements": {

            "logical_reasoning": 10.0,
            "numerical_ability": 5.0,
            "analytical_thinking": 9.0,
            "problem_solving": 10.0,
            "verbal_ability": 5.0,
            "spatial_reasoning": 5.0,
            "creative_thinking": 5.0,
            "attention_detail": 10.0,
        },

        "work_style_requirements": {

            "people_interaction": 3.0,
            "helping_others": 4.0,
            "teamwork": 6.0,
            "independent_work": 8.0,
            "leadership": 3.0,
            "data_work": 6.0,
            "technology_work": 10.0,
            "creative_work": 3.0,
            "research_work": 9.0,
            "field_work": 3.0,
            "structured_work": 8.0,
            "flexible_work": 6.0,
        },

        "core_skills": [
            "Networking",
            "Operating Systems",
            "Cybersecurity Fundamentals",
            "Security Monitoring",
            "Threat Analysis",
            "Linux",
            "Python or Scripting",
            "Incident Response",
        ],
    },


    # ========================================================
    # MEDICINE & HEALTHCARE
    # ========================================================

    "doctor": {

        "name": "Doctor",

        "domain": "Medicine & Healthcare",

        "description": (
            "Diagnoses, treats, and manages health conditions "
            "while working closely with patients."
        ),

        "education_notes": (
            "Requires a medical education pathway and the "
            "appropriate professional licensing/registration. "
            "Requirements vary by country and specialization."
        ),

        "interest_requirements": {

            "technology": 3.0,
            "mathematics": 5.0,
            "science": 10.0,
            "biology_health": 10.0,
            "business": 2.0,
            "finance": 1.0,
            "law": 1.0,
            "social_issues": 5.0,
            "public_service": 5.0,
            "communication": 8.0,
            "creative_arts": 1.0,
            "media": 1.0,
            "people_helping": 10.0,
            "research": 7.0,
            "nature_environment": 1.0,
            "physical_activity": 3.0,
        },

        "aptitude_requirements": {

            "logical_reasoning": 7.0,
            "numerical_ability": 6.0,
            "analytical_thinking": 9.0,
            "problem_solving": 9.0,
            "verbal_ability": 9.0,
            "spatial_reasoning": 5.0,
            "creative_thinking": 4.0,
            "attention_detail": 10.0,
        },

        "work_style_requirements": {

            "people_interaction": 10.0,
            "helping_others": 10.0,
            "teamwork": 8.0,
            "independent_work": 5.0,
            "leadership": 7.0,
            "data_work": 4.0,
            "technology_work": 4.0,
            "creative_work": 3.0,
            "research_work": 7.0,
            "field_work": 6.0,
            "structured_work": 8.0,
            "flexible_work": 5.0,
        },

        "core_skills": [
            "Biology",
            "Human Anatomy",
            "Clinical Reasoning",
            "Communication",
            "Patient Care",
            "Medical Knowledge",
            "Decision Making",
            "Professional Ethics",
        ],
    },


    "nurse": {

        "name": "Nurse",

        "domain": "Medicine & Healthcare",

        "description": (
            "Provides direct patient care, monitors health "
            "conditions, supports treatment, and coordinates "
            "with healthcare teams."
        ),

        "education_notes": (
            "Requires an appropriate nursing education pathway "
            "and professional registration/licensing according "
            "to the relevant jurisdiction."
        ),

        "interest_requirements": {

            "technology": 2.0,
            "mathematics": 3.0,
            "science": 8.0,
            "biology_health": 10.0,
            "business": 1.0,
            "finance": 1.0,
            "law": 1.0,
            "social_issues": 5.0,
            "public_service": 5.0,
            "communication": 9.0,
            "creative_arts": 1.0,
            "media": 1.0,
            "people_helping": 10.0,
            "research": 5.0,
            "nature_environment": 1.0,
            "physical_activity": 5.0,
        },

        "aptitude_requirements": {

            "logical_reasoning": 6.0,
            "numerical_ability": 5.0,
            "analytical_thinking": 7.0,
            "problem_solving": 8.0,
            "verbal_ability": 9.0,
            "spatial_reasoning": 4.0,
            "creative_thinking": 4.0,
            "attention_detail": 10.0,
        },

        "work_style_requirements": {

            "people_interaction": 10.0,
            "helping_others": 10.0,
            "teamwork": 9.0,
            "independent_work": 5.0,
            "leadership": 5.0,
            "data_work": 3.0,
            "technology_work": 3.0,
            "creative_work": 2.0,
            "research_work": 5.0,
            "field_work": 7.0,
            "structured_work": 9.0,
            "flexible_work": 6.0,
        },

        "core_skills": [
            "Patient Care",
            "Human Biology",
            "Communication",
            "Clinical Procedures",
            "Observation",
            "Teamwork",
            "Professional Ethics",
            "Time Management",
        ],
    },


    # ========================================================
    # LAW & JUSTICE
    # ========================================================

    "lawyer": {

        "name": "Lawyer",

        "domain": "Law & Justice",

        "description": (
            "Interprets laws, researches legal issues, "
            "advises clients, prepares arguments, and "
            "represents clients in appropriate legal settings."
        ),

        "education_notes": (
            "Requires an appropriate legal education and, "
            "where applicable, professional qualification/"
            "registration requirements."
        ),

        "interest_requirements": {

            "technology": 2.0,
            "mathematics": 2.0,
            "science": 2.0,
            "biology_health": 1.0,
            "business": 5.0,
            "finance": 4.0,
            "law": 10.0,
            "social_issues": 9.0,
            "public_service": 8.0,
            "communication": 10.0,
            "creative_arts": 3.0,
            "media": 5.0,
            "people_helping": 6.0,
            "research": 8.0,
            "nature_environment": 2.0,
            "physical_activity": 1.0,
        },

        "aptitude_requirements": {

            "logical_reasoning": 9.0,
            "numerical_ability": 4.0,
            "analytical_thinking": 9.0,
            "problem_solving": 8.0,
            "verbal_ability": 10.0,
            "spatial_reasoning": 2.0,
            "creative_thinking": 6.0,
            "attention_detail": 9.0,
        },

        "work_style_requirements": {

            "people_interaction": 9.0,
            "helping_others": 6.0,
            "teamwork": 7.0,
            "independent_work": 7.0,
            "leadership": 7.0,
            "data_work": 2.0,
            "technology_work": 2.0,
            "creative_work": 5.0,
            "research_work": 9.0,
            "field_work": 5.0,
            "structured_work": 7.0,
            "flexible_work": 7.0,
        },

        "core_skills": [
            "Legal Research",
            "Legal Writing",
            "Communication",
            "Critical Thinking",
            "Argumentation",
            "Case Analysis",
            "Negotiation",
            "Professional Ethics",
        ],
    },


    # ========================================================
    # DESIGN & CREATIVE
    # ========================================================

    "ui_ux_designer": {

        "name": "UI/UX Designer",

        "domain": "Design & Creative",

        "description": (
            "Designs user interfaces and experiences by "
            "combining creativity, user research, visual "
            "design, and problem solving."
        ),

        "education_notes": (
            "Relevant pathways include Design, Computer Science, "
            "Interaction Design, Visual Communication, or "
            "portfolio-based learning."
        ),

        "interest_requirements": {

            "technology": 7.0,
            "mathematics": 3.0,
            "science": 2.0,
            "biology_health": 1.0,
            "business": 5.0,
            "finance": 1.0,
            "law": 1.0,
            "social_issues": 4.0,
            "public_service": 2.0,
            "communication": 8.0,
            "creative_arts": 10.0,
            "media": 8.0,
            "people_helping": 5.0,
            "research": 6.0,
            "nature_environment": 2.0,
            "physical_activity": 1.0,
        },

        "aptitude_requirements": {

            "logical_reasoning": 6.0,
            "numerical_ability": 3.0,
            "analytical_thinking": 7.0,
            "problem_solving": 8.0,
            "verbal_ability": 7.0,
            "spatial_reasoning": 7.0,
            "creative_thinking": 10.0,
            "attention_detail": 9.0,
        },

        "work_style_requirements": {

            "people_interaction": 6.0,
            "helping_others": 6.0,
            "teamwork": 7.0,
            "independent_work": 7.0,
            "leadership": 3.0,
            "data_work": 4.0,
            "technology_work": 7.0,
            "creative_work": 10.0,
            "research_work": 7.0,
            "field_work": 2.0,
            "structured_work": 5.0,
            "flexible_work": 9.0,
        },

        "core_skills": [
            "UI Design",
            "UX Research",
            "Wireframing",
            "Prototyping",
            "Figma",
            "Visual Design",
            "Usability",
            "User-Centered Design",
        ],
    },

    # ========================================================
    # ADDITIONAL CAREERS (COMPACT EXPANSION)
    # ========================================================
    "web_developer": {"name":"Web Developer","domain":"Technology & Computing","description":"Builds websites and web applications.","education_notes":"CSE, IT or portfolio-based learning.","interest_requirements":{"technology":10,"mathematics":5,"science":3,"biology_health":0,"business":4,"finance":1,"law":0,"social_issues":2,"public_service":1,"communication":5,"creative_arts":6,"media":4,"people_helping":2,"research":5,"nature_environment":1,"physical_activity":1},"aptitude_requirements":{"logical_reasoning":9,"numerical_ability":5,"analytical_thinking":8,"problem_solving":9,"verbal_ability":5,"spatial_reasoning":5,"creative_thinking":7,"attention_detail":8},"work_style_requirements":{"people_interaction":4,"helping_others":2,"teamwork":6,"independent_work":8,"leadership":3,"data_work":4,"technology_work":10,"creative_work":8,"research_work":5,"field_work":1,"structured_work":7,"flexible_work":8},"core_skills":["HTML","CSS","JavaScript","React","Git","APIs","SQL","Projects"]},
    "business_analyst": {"name":"Business Analyst","domain":"Business & Management","description":"Improves business decisions using analysis.","education_notes":"Business, Economics, CSE or IT.","interest_requirements":{"technology":6,"mathematics":7,"science":2,"biology_health":1,"business":10,"finance":6,"law":2,"social_issues":3,"public_service":2,"communication":9,"creative_arts":3,"media":2,"people_helping":4,"research":8,"nature_environment":1,"physical_activity":1},"aptitude_requirements":{"logical_reasoning":8,"numerical_ability":7,"analytical_thinking":10,"problem_solving":9,"verbal_ability":9,"spatial_reasoning":2,"creative_thinking":6,"attention_detail":8},"work_style_requirements":{"people_interaction":8,"helping_others":4,"teamwork":8,"independent_work":6,"leadership":5,"data_work":7,"technology_work":6,"creative_work":5,"research_work":8,"field_work":2,"structured_work":7,"flexible_work":7},"core_skills":["Excel","SQL","Communication","Analysis","Documentation","Research","Presentation","Problem Solving"]},
    "teacher": {"name":"Teacher / Educator","domain":"Education","description":"Helps students learn and grow.","education_notes":"Qualification depends on level and country.","interest_requirements":{"technology":4,"mathematics":5,"science":5,"biology_health":3,"business":2,"finance":1,"law":1,"social_issues":6,"public_service":5,"communication":10,"creative_arts":5,"media":3,"people_helping":10,"research":6,"nature_environment":3,"physical_activity":4},"aptitude_requirements":{"logical_reasoning":6,"numerical_ability":5,"analytical_thinking":7,"problem_solving":8,"verbal_ability":10,"spatial_reasoning":3,"creative_thinking":8,"attention_detail":8},"work_style_requirements":{"people_interaction":10,"helping_others":10,"teamwork":8,"independent_work":6,"leadership":6,"data_work":3,"technology_work":4,"creative_work":7,"research_work":5,"field_work":3,"structured_work":8,"flexible_work":7},"core_skills":["Teaching","Lesson Planning","Communication","Assessment","Empathy","Presentation","Classroom Management","Subject Knowledge"]},
}


# ============================================================
# 2. EXPECTED DIMENSIONS
# ============================================================

EXPECTED_INTEREST_DIMENSIONS = {

    "technology",
    "mathematics",
    "science",
    "biology_health",
    "business",
    "finance",
    "law",
    "social_issues",
    "public_service",
    "communication",
    "creative_arts",
    "media",
    "people_helping",
    "research",
    "nature_environment",
    "physical_activity",
}


EXPECTED_APTITUDE_DIMENSIONS = {

    "logical_reasoning",
    "numerical_ability",
    "analytical_thinking",
    "problem_solving",
    "verbal_ability",
    "spatial_reasoning",
    "creative_thinking",
    "attention_detail",
}


EXPECTED_WORK_STYLE_DIMENSIONS = {

    "people_interaction",
    "helping_others",
    "teamwork",
    "independent_work",
    "leadership",
    "data_work",
    "technology_work",
    "creative_work",
    "research_work",
    "field_work",
    "structured_work",
    "flexible_work",
}


# ============================================================
# 3. VALIDATE CAREER PROFILES
# ============================================================

def validate_career_profiles():
    """
    Validate the complete career knowledge base.

    Checks:

        1. Career IDs are valid.
        2. Career names exist.
        3. Domains exist.
        4. All interest dimensions exist.
        5. All aptitude dimensions exist.
        6. All work-style dimensions exist.
        7. Requirement values are between 0 and 10.
        8. Core skills are present.
    """

    if not CAREER_PROFILES:

        raise ValueError(
            "No career profiles found."
        )

    for career_id, career in (
        CAREER_PROFILES.items()
    ):

        # ----------------------------------------------------
        # Basic fields
        # ----------------------------------------------------

        required_fields = {
            "name",
            "domain",
            "description",
            "education_notes",
            "interest_requirements",
            "aptitude_requirements",
            "work_style_requirements",
            "core_skills",
        }

        missing_fields = (
            required_fields
            - set(career.keys())
        )

        if missing_fields:

            raise ValueError(
                f"{career_id} is missing fields: "
                f"{sorted(missing_fields)}"
            )

        # ----------------------------------------------------
        # Interest dimensions
        # ----------------------------------------------------

        interest_dimensions = set(
            career[
                "interest_requirements"
            ].keys()
        )

        if (
            interest_dimensions
            != EXPECTED_INTEREST_DIMENSIONS
        ):

            missing = (
                EXPECTED_INTEREST_DIMENSIONS
                - interest_dimensions
            )

            extra = (
                interest_dimensions
                - EXPECTED_INTEREST_DIMENSIONS
            )

            raise ValueError(
                f"{career_id} interest dimensions "
                f"are incorrect. "
                f"Missing={sorted(missing)}, "
                f"Extra={sorted(extra)}"
            )

        # ----------------------------------------------------
        # Aptitude dimensions
        # ----------------------------------------------------

        aptitude_dimensions = set(
            career[
                "aptitude_requirements"
            ].keys()
        )

        if (
            aptitude_dimensions
            != EXPECTED_APTITUDE_DIMENSIONS
        ):

            missing = (
                EXPECTED_APTITUDE_DIMENSIONS
                - aptitude_dimensions
            )

            extra = (
                aptitude_dimensions
                - EXPECTED_APTITUDE_DIMENSIONS
            )

            raise ValueError(
                f"{career_id} aptitude dimensions "
                f"are incorrect. "
                f"Missing={sorted(missing)}, "
                f"Extra={sorted(extra)}"
            )

        # ----------------------------------------------------
        # Work-style dimensions
        # ----------------------------------------------------

        work_style_dimensions = set(
            career[
                "work_style_requirements"
            ].keys()
        )

        if (
            work_style_dimensions
            != EXPECTED_WORK_STYLE_DIMENSIONS
        ):

            missing = (
                EXPECTED_WORK_STYLE_DIMENSIONS
                - work_style_dimensions
            )

            extra = (
                work_style_dimensions
                - EXPECTED_WORK_STYLE_DIMENSIONS
            )

            raise ValueError(
                f"{career_id} work-style dimensions "
                f"are incorrect. "
                f"Missing={sorted(missing)}, "
                f"Extra={sorted(extra)}"
            )

        # ----------------------------------------------------
        # Validate requirement ranges
        # ----------------------------------------------------

        requirement_groups = [
            career[
                "interest_requirements"
            ],
            career[
                "aptitude_requirements"
            ],
            career[
                "work_style_requirements"
            ],
        ]

        for group in requirement_groups:

            for dimension, value in group.items():

                if not isinstance(
                    value,
                    (int, float),
                ):

                    raise ValueError(
                        f"{career_id}: "
                        f"{dimension} must be numeric."
                    )

                if value < 0 or value > 10:

                    raise ValueError(
                        f"{career_id}: "
                        f"{dimension} must be "
                        f"between 0 and 10."
                    )

        # ----------------------------------------------------
        # Core skills
        # ----------------------------------------------------

        if not isinstance(
            career["core_skills"],
            list,
        ):

            raise ValueError(
                f"{career_id}: core_skills "
                f"must be a list."
            )

        if len(
            career["core_skills"]
        ) == 0:

            raise ValueError(
                f"{career_id}: core_skills "
                f"cannot be empty."
            )

    return True


# ============================================================
# 4. GET CAREER
# ============================================================

def get_career_profile(career_id):
    """
    Return a single career profile.
    """

    if career_id not in CAREER_PROFILES:

        raise ValueError(
            f"Unknown career: {career_id}"
        )

    return CAREER_PROFILES[career_id]


# ============================================================
# 5. GET ALL CAREERS
# ============================================================

def get_all_career_profiles():
    """
    Return all career profiles.
    """

    return CAREER_PROFILES


# ============================================================
# 6. GET CAREER NAMES
# ============================================================

def get_career_names():
    """
    Return career names.
    """

    return [
        career["name"]
        for career in CAREER_PROFILES.values()
    ]


# ============================================================
# 7. TEST
# ============================================================

if __name__ == "__main__":

    validate_career_profiles()

    print(
        "Career profile validation successful."
    )

    print(
        f"Number of careers: "
        f"{len(CAREER_PROFILES)}"
    )

    print()

    for career_id, career in (
        CAREER_PROFILES.items()
    ):

        print(
            f"- {career['name']} "
            f"({career['domain']})"
        )

    print()

    # --------------------------------------------------------
    # Show one example profile
    # --------------------------------------------------------

    example = get_career_profile(
        "software_developer"
    )

    print("=" * 70)
    print("EXAMPLE CAREER PROFILE")
    print("=" * 70)

    print(
        f"Career: {example['name']}"
    )

    print(
        f"Domain: {example['domain']}"
    )

    print()

    print("Interest requirements:")

    for dimension, value in (
        example[
            "interest_requirements"
        ].items()
    ):

        print(
            f"  {dimension:20} {value:4.1f}/10"
        )

    print()

    print("Aptitude requirements:")

    for dimension, value in (
        example[
            "aptitude_requirements"
        ].items()
    ):

        print(
            f"  {dimension:20} {value:4.1f}/10"
        )

    print()

    print("Work-style requirements:")

    for dimension, value in (
        example[
            "work_style_requirements"
        ].items()
    ):

        print(
            f"  {dimension:20} {value:4.1f}/10"
        )

    print()

    print("Core skills:")

    for skill in example[
        "core_skills"
    ]:

        print(
            f"  - {skill}"
        )
