"""
Roadmap Knowledge Base
----------------------

Defines structured learning pathways for the careers
currently supported by Student Career Navigator.

This file contains KNOWLEDGE about career development.

It does NOT personalize a student's roadmap.

Personalization will be handled later by roadmap.py.

Structure:

Career
    ↓
Stages
    ↓
Skills
    ↓
Prerequisites
    ↓
Practice
    ↓
Projects / experience
"""


# ============================================================
# ROADMAPS
# ============================================================

ROADMAPS = {

    # ========================================================
    # SOFTWARE DEVELOPER
    # ========================================================

    "software_developer": {

        "career_name": "Software Developer",

        "domain": "Technology & Computing",

        "description": (
            "Builds software applications by combining "
            "programming, problem solving, software engineering, "
            "and practical development skills."
        ),

        "stages": [

            {
                "stage_id": "programming_foundations",

                "title": "Programming Foundations",

                "purpose": (
                    "Build a strong foundation in programming "
                    "before moving into larger software projects."
                ),

                "skills": [
                    "programming_fundamentals",
                    "problem_solving",
                    "debugging",
                ],

                "prerequisites": [],

                "practice": [
                    "Solve small programming problems.",
                    "Practice variables, conditions, loops, and functions.",
                    "Debug simple programs."
                ],

                "project": (
                    "Build a small command-line application."
                ),
            },

            {
                "stage_id": "data_structures",

                "title": "Data Structures & Algorithms",

                "purpose": (
                    "Develop efficient problem-solving ability "
                    "using common data structures and algorithms."
                ),

                "skills": [
                    "data_structures",
                    "algorithms",
                    "logical_reasoning",
                    "problem_solving",
                ],

                "prerequisites": [
                    "programming_foundations"
                ],

                "practice": [
                    "Practice arrays, strings, stacks, queues, and trees.",
                    "Solve algorithmic problems.",
                    "Analyze basic time complexity."
                ],

                "project": (
                    "Build a project that uses multiple "
                    "data structures."
                ),
            },

            {
                "stage_id": "development_tools",

                "title": "Development Tools",

                "purpose": (
                    "Learn the tools used to manage and "
                    "develop real software projects."
                ),

                "skills": [
                    "git",
                    "github",
                    "version_control",
                    "development_environment",
                ],

                "prerequisites": [
                    "programming_foundations"
                ],

                "practice": [
                    "Use Git for version control.",
                    "Create and manage GitHub repositories.",
                    "Practice branching and commits."
                ],

                "project": (
                    "Publish a software project on GitHub "
                    "with proper documentation."
                ),
            },

            {
                "stage_id": "software_engineering",

                "title": "Software Engineering",

                "purpose": (
                    "Understand how larger software systems "
                    "are designed, developed, tested, and maintained."
                ),

                "skills": [
                    "software_design",
                    "testing",
                    "debugging",
                    "documentation",
                ],

                "prerequisites": [
                    "programming_foundations",
                    "development_tools"
                ],

                "practice": [
                    "Write modular code.",
                    "Practice unit testing.",
                    "Learn basic software architecture."
                ],

                "project": (
                    "Build a medium-sized application "
                    "with multiple components."
                ),
            },

            {
                "stage_id": "portfolio",

                "title": "Portfolio & Real-World Experience",

                "purpose": (
                    "Turn technical knowledge into demonstrable "
                    "experience."
                ),

                "skills": [
                    "project_development",
                    "documentation",
                    "communication",
                ],

                "prerequisites": [
                    "software_engineering"
                ],

                "practice": [
                    "Improve project documentation.",
                    "Explain technical decisions.",
                    "Practice presenting projects."
                ],

                "project": (
                    "Build 2–3 portfolio-quality projects "
                    "and publish them on GitHub."
                ),
            },
        ],
    },


    # ========================================================
    # DATA ANALYST
    # ========================================================

    "data_analyst": {

        "career_name": "Data Analyst",

        "domain": "Technology & Computing",

        "description": (
            "Analyzes data to identify patterns, answer "
            "questions, create reports, and support decisions."
        ),

        "stages": [

            {
                "stage_id": "data_foundations",

                "title": "Data Foundations",

                "purpose": (
                    "Understand basic data concepts and "
                    "quantitative reasoning."
                ),

                "skills": [
                    "statistics",
                    "numerical_ability",
                    "data_literacy",
                ],

                "prerequisites": [],

                "practice": [
                    "Practice descriptive statistics.",
                    "Understand averages, distributions, and variation.",
                    "Interpret simple datasets."
                ],

                "project": (
                    "Analyze a small public dataset "
                    "using basic statistics."
                ),
            },

            {
                "stage_id": "spreadsheet_analysis",

                "title": "Spreadsheet Analysis",

                "purpose": (
                    "Develop practical skills for organizing "
                    "and analyzing tabular data."
                ),

                "skills": [
                    "excel",
                    "data_cleaning",
                    "data_analysis",
                ],

                "prerequisites": [
                    "data_foundations"
                ],

                "practice": [
                    "Use formulas and functions.",
                    "Create pivot tables.",
                    "Clean messy spreadsheet data."
                ],

                "project": (
                    "Create an analytical dashboard "
                    "using spreadsheet data."
                ),
            },

            {
                "stage_id": "sql",

                "title": "SQL & Database Analysis",

                "purpose": (
                    "Learn to retrieve and analyze data "
                    "from relational databases."
                ),

                "skills": [
                    "sql",
                    "databases",
                    "data_querying",
                ],

                "prerequisites": [
                    "data_foundations"
                ],

                "practice": [
                    "Write SELECT queries.",
                    "Practice filtering and grouping.",
                    "Learn joins and subqueries."
                ],

                "project": (
                    "Analyze a relational database "
                    "using SQL."
                ),
            },

            {
                "stage_id": "python_analysis",

                "title": "Python for Data Analysis",

                "purpose": (
                    "Use Python to clean, analyze, and "
                    "manipulate datasets."
                ),

                "skills": [
                    "python",
                    "pandas",
                    "data_cleaning",
                ],

                "prerequisites": [
                    "data_foundations"
                ],

                "practice": [
                    "Learn Python data structures.",
                    "Use Pandas for data manipulation.",
                    "Clean missing and inconsistent data."
                ],

                "project": (
                    "Perform an end-to-end analysis "
                    "of a real dataset."
                ),
            },

            {
                "stage_id": "visualization",

                "title": "Data Visualization",

                "purpose": (
                    "Communicate findings through effective "
                    "charts and dashboards."
                ),

                "skills": [
                    "data_visualization",
                    "matplotlib",
                    "plotly",
                    "dashboarding",
                ],

                "prerequisites": [
                    "python_analysis"
                ],

                "practice": [
                    "Create appropriate charts.",
                    "Compare different visualization techniques.",
                    "Build interactive dashboards."
                ],

                "project": (
                    "Create an interactive data dashboard."
                ),
            },

            {
                "stage_id": "portfolio",

                "title": "Analytics Portfolio",

                "purpose": (
                    "Demonstrate practical analytical ability "
                    "through real projects."
                ),

                "skills": [
                    "data_analysis",
                    "communication",
                    "storytelling",
                ],

                "prerequisites": [
                    "sql",
                    "python_analysis",
                    "visualization"
                ],

                "practice": [
                    "Explain analytical findings clearly.",
                    "Document projects.",
                    "Publish projects on GitHub."
                ],

                "project": (
                    "Build 2–3 complete analytics projects."
                ),
            },
        ],
    },


    # ========================================================
    # DATA SCIENTIST
    # ========================================================

    "data_scientist": {

        "career_name": "Data Scientist",

        "domain": "Technology & Computing",

        "description": (
            "Uses statistics, programming, data analysis, "
            "and machine learning to extract insights and "
            "build predictive models."
        ),

        "stages": [

            {
                "stage_id": "mathematical_foundations",

                "title": "Mathematical & Statistical Foundations",

                "purpose": (
                    "Build the mathematical foundation required "
                    "for data analysis and machine learning."
                ),

                "skills": [
                    "statistics",
                    "probability",
                    "mathematics",
                    "linear_algebra",
                ],

                "prerequisites": [],

                "practice": [
                    "Study descriptive and inferential statistics.",
                    "Learn probability fundamentals.",
                    "Practice mathematical reasoning."
                ],

                "project": (
                    "Perform statistical analysis on a dataset."
                ),
            },

            {
                "stage_id": "python",

                "title": "Python for Data Science",

                "purpose": (
                    "Develop strong Python skills for "
                    "data manipulation and analysis."
                ),

                "skills": [
                    "python",
                    "programming_fundamentals",
                ],

                "prerequisites": [
                    "mathematical_foundations"
                ],

                "practice": [
                    "Practice Python programming.",
                    "Work with functions and modules.",
                    "Write reusable data-processing code."
                ],

                "project": (
                    "Build a Python-based data analysis project."
                ),
            },

            {
                "stage_id": "data_analysis",

                "title": "Data Analysis",

                "purpose": (
                    "Learn to clean, explore, and understand "
                    "real-world datasets."
                ),

                "skills": [
                    "pandas",
                    "data_cleaning",
                    "exploratory_data_analysis",
                    "data_visualization",
                ],

                "prerequisites": [
                    "python"
                ],

                "practice": [
                    "Clean real-world datasets.",
                    "Perform exploratory data analysis.",
                    "Create meaningful visualizations."
                ],

                "project": (
                    "Complete an exploratory data analysis project."
                ),
            },

            {
                "stage_id": "sql",

                "title": "SQL & Data Management",

                "purpose": (
                    "Learn to work with structured data "
                    "stored in databases."
                ),

                "skills": [
                    "sql",
                    "databases",
                ],

                "prerequisites": [
                    "data_analysis"
                ],

                "practice": [
                    "Write complex SQL queries.",
                    "Practice joins and aggregation.",
                    "Work with relational datasets."
                ],

                "project": (
                    "Analyze a multi-table database."
                ),
            },

            {
                "stage_id": "machine_learning",

                "title": "Machine Learning",

                "purpose": (
                    "Learn how predictive models are trained, "
                    "evaluated, and improved."
                ),

                "skills": [
                    "machine_learning",
                    "model_evaluation",
                    "feature_engineering",
                ],

                "prerequisites": [
                    "mathematical_foundations",
                    "data_analysis",
                    "python"
                ],

                "practice": [
                    "Learn supervised learning.",
                    "Learn unsupervised learning.",
                    "Practice model evaluation."
                ],

                "project": (
                    "Build a machine-learning prediction project."
                ),
            },

            {
                "stage_id": "advanced_ml",

                "title": "Advanced Machine Learning",

                "purpose": (
                    "Explore more advanced machine-learning "
                    "techniques and practical workflows."
                ),

                "skills": [
                    "advanced_machine_learning",
                    "model_optimization",
                    "experimentation",
                ],

                "prerequisites": [
                    "machine_learning"
                ],

                "practice": [
                    "Experiment with multiple models.",
                    "Compare model performance.",
                    "Practice feature engineering."
                ],

                "project": (
                    "Build and compare multiple machine-learning "
                    "models on a real dataset."
                ),
            },

            {
                "stage_id": "portfolio",

                "title": "Data Science Portfolio",

                "purpose": (
                    "Demonstrate complete data-science workflows "
                    "through practical projects."
                ),

                "skills": [
                    "project_development",
                    "communication",
                    "research",
                ],

                "prerequisites": [
                    "machine_learning",
                    "advanced_ml"
                ],

                "practice": [
                    "Document experiments.",
                    "Explain model decisions.",
                    "Publish projects."
                ],

                "project": (
                    "Build 2–3 portfolio-quality data-science projects."
                ),
            },
        ],
    },


    # ========================================================
    # CYBERSECURITY ANALYST
    # ========================================================

    "cybersecurity_analyst": {

        "career_name": "Cybersecurity Analyst",

        "domain": "Technology & Computing",

        "description": (
            "Helps protect systems and networks by identifying "
            "security risks, monitoring activity, and responding "
            "to security incidents."
        ),

        "stages": [

            {
                "stage_id": "computing_foundations",

                "title": "Computing Foundations",

                "purpose": (
                    "Build a strong understanding of computers, "
                    "operating systems, and networks."
                ),

                "skills": [
                    "programming_fundamentals",
                    "operating_systems",
                    "computer_networks",
                ],

                "prerequisites": [],

                "practice": [
                    "Learn operating-system concepts.",
                    "Study networking fundamentals.",
                    "Practice basic command-line operations."
                ],

                "project": (
                    "Set up a small local network lab."
                ),
            },

            {
                "stage_id": "network_security",

                "title": "Networking & Security Fundamentals",

                "purpose": (
                    "Understand how networks work and "
                    "where common security risks arise."
                ),

                "skills": [
                    "network_security",
                    "networking",
                    "security_fundamentals",
                ],

                "prerequisites": [
                    "computing_foundations"
                ],

                "practice": [
                    "Study common network protocols.",
                    "Understand authentication and access control.",
                    "Learn basic security principles."
                ],

                "project": (
                    "Document and analyze a small "
                    "network security scenario."
                ),
            },

            {
                "stage_id": "linux",

                "title": "Linux & Security Tools",

                "purpose": (
                    "Develop practical skills with Linux "
                    "and common security tools."
                ),

                "skills": [
                    "linux",
                    "command_line",
                    "security_tools",
                ],

                "prerequisites": [
                    "network_security"
                ],

                "practice": [
                    "Use Linux command-line tools.",
                    "Explore security monitoring tools.",
                    "Practice system administration basics."
                ],

                "project": (
                    "Create a small security monitoring lab."
                ),
            },

            {
                "stage_id": "security_analysis",

                "title": "Security Analysis",

                "purpose": (
                    "Learn how to identify, investigate, "
                    "and document security events."
                ),

                "skills": [
                    "threat_analysis",
                    "incident_response",
                    "security_analysis",
                ],

                "prerequisites": [
                    "linux"
                ],

                "practice": [
                    "Analyze security scenarios.",
                    "Practice incident documentation.",
                    "Study common attack patterns."
                ],

                "project": (
                    "Perform a controlled security-analysis case study."
                ),
            },

            {
                "stage_id": "security_automation",

                "title": "Security Automation",

                "purpose": (
                    "Use programming and automation to "
                    "improve security workflows."
                ),

                "skills": [
                    "python",
                    "automation",
                    "scripting",
                ],

                "prerequisites": [
                    "security_analysis"
                ],

                "practice": [
                    "Write simple security scripts.",
                    "Automate repetitive analysis tasks.",
                    "Process security logs."
                ],

                "project": (
                    "Build a defensive security automation tool."
                ),
            },

            {
                "stage_id": "portfolio",

                "title": "Security Portfolio",

                "purpose": (
                    "Demonstrate security knowledge through "
                    "documented and ethical projects."
                ),

                "skills": [
                    "security_projects",
                    "documentation",
                    "communication",
                ],

                "prerequisites": [
                    "security_analysis",
                    "security_automation"
                ],

                "practice": [
                    "Document security case studies.",
                    "Explain security decisions.",
                    "Publish safe educational projects."
                ],

                "project": (
                    "Create a portfolio containing "
                    "2–3 ethical cybersecurity projects."
                ),
            },
        ],
    },


    # ========================================================
    # UI/UX DESIGNER
    # ========================================================

    "ui_ux_designer": {

        "career_name": "UI/UX Designer",

        "domain": "Design & Creative",

        "description": (
            "Designs digital interfaces and experiences by "
            "understanding users, solving design problems, "
            "and creating usable visual solutions."
        ),

        "stages": [

            {
                "stage_id": "design_foundations",

                "title": "Design Foundations",

                "purpose": (
                    "Develop fundamental visual and design "
                    "principles."
                ),

                "skills": [
                    "design_principles",
                    "visual_design",
                    "creative_thinking",
                ],

                "prerequisites": [],

                "practice": [
                    "Study layout, hierarchy, spacing, and typography.",
                    "Analyze existing interfaces.",
                    "Practice visual composition."
                ],

                "project": (
                    "Redesign a simple digital interface."
                ),
            },

            {
                "stage_id": "user_research",

                "title": "User Research",

                "purpose": (
                    "Understand users and identify problems "
                    "worth solving."
                ),

                "skills": [
                    "user_research",
                    "empathy",
                    "problem_solving",
                ],

                "prerequisites": [
                    "design_foundations"
                ],

                "practice": [
                    "Conduct simple user interviews.",
                    "Create user personas.",
                    "Identify user pain points."
                ],

                "project": (
                    "Conduct a small user-research study."
                ),
            },

            {
                "stage_id": "wireframing",

                "title": "Wireframing & Prototyping",

                "purpose": (
                    "Translate user needs into interface "
                    "structures and prototypes."
                ),

                "skills": [
                    "wireframing",
                    "prototyping",
                    "interaction_design",
                ],

                "prerequisites": [
                    "user_research"
                ],

                "practice": [
                    "Create low-fidelity wireframes.",
                    "Create clickable prototypes.",
                    "Test different interaction flows."
                ],

                "project": (
                    "Design a complete application flow."
                ),
            },

            {
                "stage_id": "ui_design",

                "title": "UI Design",

                "purpose": (
                    "Create polished and consistent "
                    "digital interfaces."
                ),

                "skills": [
                    "ui_design",
                    "typography",
                    "color_theory",
                    "design_systems",
                ],

                "prerequisites": [
                    "wireframing"
                ],

                "practice": [
                    "Create high-fidelity screens.",
                    "Develop consistent visual systems.",
                    "Practice responsive design."
                ],

                "project": (
                    "Design a complete multi-screen application."
                ),
            },

            {
                "stage_id": "usability_testing",

                "title": "Usability Testing",

                "purpose": (
                    "Learn how to evaluate whether designs "
                    "actually work for users."
                ),

                "skills": [
                    "usability_testing",
                    "feedback_analysis",
                    "iteration",
                ],

                "prerequisites": [
                    "ui_design"
                ],

                "practice": [
                    "Conduct usability tests.",
                    "Collect user feedback.",
                    "Iterate on designs."
                ],

                "project": (
                    "Test and improve an existing prototype."
                ),
            },

            {
                "stage_id": "portfolio",

                "title": "Design Portfolio",

                "purpose": (
                    "Demonstrate design thinking and practical "
                    "work through case studies."
                ),

                "skills": [
                    "portfolio_design",
                    "storytelling",
                    "communication",
                ],

                "prerequisites": [
                    "usability_testing"
                ],

                "practice": [
                    "Write design case studies.",
                    "Explain design decisions.",
                    "Present before-and-after iterations."
                ],

                "project": (
                    "Build a portfolio containing 2–3 "
                    "complete UX case studies."
                ),
            },
        ],
    },


    # ========================================================
    # DOCTOR
    # ========================================================

    "doctor": {

        "career_name": "Doctor",

        "domain": "Medicine & Healthcare",

        "description": (
            "Diagnoses and manages health conditions through "
            "medical knowledge, clinical reasoning, and patient care."
        ),

        "stages": [

            {
                "stage_id": "science_foundations",

                "title": "Science Foundations",

                "purpose": (
                    "Build a strong foundation in biology, "
                    "chemistry, and related sciences."
                ),

                "skills": [
                    "biology",
                    "chemistry",
                    "scientific_reasoning",
                ],

                "prerequisites": [],

                "practice": [
                    "Strengthen biology fundamentals.",
                    "Study core chemistry concepts.",
                    "Practice scientific reasoning."
                ],

                "project": (
                    "Complete a structured science investigation "
                    "or academic project."
                ),
            },

            {
                "stage_id": "medical_foundations",

                "title": "Medical Foundations",

                "purpose": (
                    "Build foundational knowledge of the "
                    "human body and medical science."
                ),

                "skills": [
                    "anatomy",
                    "physiology",
                    "pathology",
                ],

                "prerequisites": [
                    "science_foundations"
                ],

                "practice": [
                    "Study human anatomy.",
                    "Understand basic physiology.",
                    "Learn introductory pathology."
                ],

                "project": (
                    "Create a structured educational "
                    "medical-science presentation."
                ),
            },

            {
                "stage_id": "clinical_reasoning",

                "title": "Clinical Reasoning",

                "purpose": (
                    "Develop the ability to interpret information "
                    "and reason through clinical situations."
                ),

                "skills": [
                    "clinical_reasoning",
                    "decision_making",
                    "analytical_thinking",
                ],

                "prerequisites": [
                    "medical_foundations"
                ],

                "practice": [
                    "Study clinical case scenarios.",
                    "Practice structured reasoning.",
                    "Compare possible explanations."
                ],

                "project": (
                    "Analyze educational clinical case studies."
                ),
            },

            {
                "stage_id": "communication",

                "title": "Patient Communication",

                "purpose": (
                    "Develop effective and empathetic "
                    "communication with patients."
                ),

                "skills": [
                    "communication",
                    "empathy",
                    "patient_communication",
                ],

                "prerequisites": [
                    "clinical_reasoning"
                ],

                "practice": [
                    "Practice active listening.",
                    "Practice explaining complex ideas simply.",
                    "Develop empathetic communication."
                ],

                "project": (
                    "Create a patient-education communication exercise."
                ),
            },

            {
                "stage_id": "clinical_training",

                "title": "Clinical Training",

                "purpose": (
                    "Develop practical clinical skills through "
                    "formal medical education and supervised training."
                ),

                "skills": [
                    "clinical_skills",
                    "patient_care",
                    "attention_to_detail",
                ],

                "prerequisites": [
                    "clinical_reasoning",
                    "communication"
                ],

                "practice": [
                    "Participate in supervised clinical training.",
                    "Practice clinical procedures only in appropriate "
                    "educational settings."
                ],

                "project": (
                    "Maintain a structured clinical-learning portfolio."
                ),
            },

            {
                "stage_id": "professional_development",

                "title": "Professional Development",

                "purpose": (
                    "Continue developing medical knowledge, "
                    "professional communication, and specialization."
                ),

                "skills": [
                    "professionalism",
                    "research",
                    "continuous_learning",
                ],

                "prerequisites": [
                    "clinical_training"
                ],

                "practice": [
                    "Read current medical literature.",
                    "Develop professional communication.",
                    "Explore medical specializations."
                ],

                "project": (
                    "Build a structured academic or research portfolio."
                ),
            },
        ],
    },


    # ========================================================
    # NURSE
    # ========================================================

    "nurse": {

        "career_name": "Nurse",

        "domain": "Medicine & Healthcare",

        "description": (
            "Provides patient care, supports treatment, "
            "monitors health conditions, and works as part "
            "of a healthcare team."
        ),

        "stages": [

            {
                "stage_id": "science_foundations",

                "title": "Science Foundations",

                "purpose": (
                    "Build foundational knowledge in biology "
                    "and health sciences."
                ),

                "skills": [
                    "biology",
                    "health_science",
                ],

                "prerequisites": [],

                "practice": [
                    "Strengthen biology fundamentals.",
                    "Study basic health science concepts."
                ],

                "project": (
                    "Complete a health-science academic project."
                ),
            },

            {
                "stage_id": "anatomy",

                "title": "Anatomy & Physiology",

                "purpose": (
                    "Understand the structure and functioning "
                    "of the human body."
                ),

                "skills": [
                    "anatomy",
                    "physiology",
                ],

                "prerequisites": [
                    "science_foundations"
                ],

                "practice": [
                    "Study major body systems.",
                    "Connect anatomy with basic physiology."
                ],

                "project": (
                    "Create a structured anatomy learning portfolio."
                ),
            },

            {
                "stage_id": "patient_care",

                "title": "Patient Care Foundations",

                "purpose": (
                    "Develop foundational knowledge of patient "
                    "care and healthcare support."
                ),

                "skills": [
                    "patient_care",
                    "attention_to_detail",
                    "clinical_skills",
                ],

                "prerequisites": [
                    "anatomy"
                ],

                "practice": [
                    "Learn patient-care concepts through "
                    "formal education.",
                    "Practice appropriate documentation."
                ],

                "project": (
                    "Create an educational patient-care case study."
                ),
            },

            {
                "stage_id": "communication",

                "title": "Patient Communication",

                "purpose": (
                    "Develop communication and interpersonal "
                    "skills needed in patient-centered care."
                ),

                "skills": [
                    "patient_communication",
                    "empathy",
                    "communication",
                ],

                "prerequisites": [
                    "patient_care"
                ],

                "practice": [
                    "Practice active listening.",
                    "Develop empathetic communication.",
                    "Practice explaining information clearly."
                ],

                "project": (
                    "Complete a patient-communication role-play "
                    "or educational exercise."
                ),
            },

            {
                "stage_id": "teamwork",

                "title": "Healthcare Teamwork",

                "purpose": (
                    "Develop the collaboration skills needed "
                    "to work within healthcare teams."
                ),

                "skills": [
                    "teamwork",
                    "professionalism",
                    "communication",
                ],

                "prerequisites": [
                    "communication"
                ],

                "practice": [
                    "Participate in team activities.",
                    "Practice structured communication."
                ],

                "project": (
                    "Complete a healthcare teamwork case study."
                ),
            },

            {
                "stage_id": "clinical_training",

                "title": "Clinical Training",

                "purpose": (
                    "Apply knowledge through formal supervised "
                    "nursing education and clinical experience."
                ),

                "skills": [
                    "clinical_skills",
                    "patient_care",
                    "decision_making",
                    "stress_management",
                ],

                "prerequisites": [
                    "patient_care",
                    "teamwork"
                ],

                "practice": [
                    "Complete formal clinical training.",
                    "Develop professional nursing practice "
                    "under appropriate supervision."
                ],

                "project": (
                    "Maintain a structured clinical-learning portfolio."
                ),
            },
        ],
    },


    # ========================================================
    # LAWYER
    # ========================================================

    "lawyer": {

        "career_name": "Lawyer",

        "domain": "Law & Justice",

        "description": (
            "Uses legal knowledge, reasoning, research, "
            "and communication to advise clients and "
            "work with legal matters."
        ),

        "stages": [

            {
                "stage_id": "communication_foundations",

                "title": "Communication Foundations",

                "purpose": (
                    "Build strong reading, writing, and "
                    "verbal communication skills."
                ),

                "skills": [
                    "verbal_ability",
                    "written_communication",
                    "communication",
                ],

                "prerequisites": [],

                "practice": [
                    "Read articles and legal-style arguments.",
                    "Practice structured writing.",
                    "Practice speaking clearly."
                ],

                "project": (
                    "Write and present a structured argument."
                ),
            },

            {
                "stage_id": "legal_foundations",

                "title": "Legal Foundations",

                "purpose": (
                    "Develop foundational understanding of "
                    "legal systems and concepts."
                ),

                "skills": [
                    "legal_knowledge",
                    "law",
                    "civics",
                ],

                "prerequisites": [
                    "communication_foundations"
                ],

                "practice": [
                    "Study basic legal concepts.",
                    "Understand legal institutions.",
                    "Follow important legal developments."
                ],

                "project": (
                    "Create a structured legal-topic report."
                ),
            },

            {
                "stage_id": "legal_reasoning",

                "title": "Legal Reasoning",

                "purpose": (
                    "Develop the ability to interpret facts "
                    "and apply legal reasoning."
                ),

                "skills": [
                    "logical_reasoning",
                    "analytical_thinking",
                    "problem_solving",
                ],

                "prerequisites": [
                    "legal_foundations"
                ],

                "practice": [
                    "Analyze case scenarios.",
                    "Identify relevant facts.",
                    "Construct logical arguments."
                ],

                "project": (
                    "Analyze an educational legal case study."
                ),
            },

            {
                "stage_id": "legal_research",

                "title": "Legal Research",

                "purpose": (
                    "Learn to find, evaluate, and organize "
                    "legal information."
                ),

                "skills": [
                    "research",
                    "information_analysis",
                    "attention_to_detail",
                ],

                "prerequisites": [
                    "legal_reasoning"
                ],

                "practice": [
                    "Research legal sources.",
                    "Compare arguments.",
                    "Summarize legal information."
                ],

                "project": (
                    "Produce a structured legal research report."
                ),
            },

            {
                "stage_id": "advocacy",

                "title": "Advocacy & Negotiation",

                "purpose": (
                    "Develop communication and argumentation "
                    "skills for practical legal work."
                ),

                "skills": [
                    "public_speaking",
                    "negotiation",
                    "persuasion",
                ],

                "prerequisites": [
                    "legal_research"
                ],

                "practice": [
                    "Practice structured arguments.",
                    "Participate in debates or mock exercises.",
                    "Develop negotiation skills."
                ],

                "project": (
                    "Participate in a mock legal argument or debate."
                ),
            },

            {
                "stage_id": "professional_experience",

                "title": "Professional Legal Experience",

                "purpose": (
                    "Gain practical exposure to legal work "
                    "through appropriate education and internships."
                ),

                "skills": [
                    "professionalism",
                    "legal_writing",
                    "client_communication",
                ],

                "prerequisites": [
                    "advocacy"
                ],

                "practice": [
                    "Complete appropriate internships.",
                    "Observe legal professionals.",
                    "Develop professional documentation."
                ],

                "project": (
                    "Build a portfolio of legal research, "
                    "writing, and academic work."
                ),
            },
        ],
    },

    # ========================================================
    # WEB DEVELOPER
    # ========================================================

    "web_developer": {

        "career_name": "Web Developer",

        "domain": "Technology & Computing",

        "description": (
            "Builds and maintains websites and web applications "
            "using frontend and backend technologies."
        ),

        "stages": [

            {
                "stage_id": "web_foundations",

                "title": "Web Foundations",

                "purpose": (
                    "Build a strong foundation in how websites "
                    "and web applications work."
                ),

                "skills": [
                    "html",
                    "css",
                    "web_fundamentals",
                ],

                "prerequisites": [],

                "practice": [
                    "Learn HTML structure and semantic elements.",
                    "Practice CSS layouts, spacing, and responsive design.",
                    "Build simple static web pages.",
                ],

                "project": (
                    "Build a responsive personal profile website."
                ),
            },

            {
                "stage_id": "javascript",

                "title": "JavaScript & Interactivity",

                "purpose": (
                    "Learn to make websites interactive and "
                    "responsive to user actions."
                ),

                "skills": [
                    "javascript",
                    "programming",
                    "problem_solving",
                ],

                "prerequisites": [
                    "web_foundations",
                ],

                "practice": [
                    "Learn variables, functions, arrays, and objects.",
                    "Practice DOM manipulation and events.",
                    "Build small interactive web features.",
                ],

                "project": (
                    "Build an interactive JavaScript web application."
                ),
            },

            {
                "stage_id": "development_tools",

                "title": "Development Tools",

                "purpose": (
                    "Learn the tools used in real web development "
                    "projects."
                ),

                "skills": [
                    "git",
                    "github",
                    "version_control",
                ],

                "prerequisites": [
                    "javascript",
                ],

                "practice": [
                    "Learn Git fundamentals.",
                    "Create and manage GitHub repositories.",
                    "Practice commits, branches, and pull requests.",
                ],

                "project": (
                    "Publish a web project on GitHub with documentation."
                ),
            },

            {
                "stage_id": "frontend_development",

                "title": "Frontend Development",

                "purpose": (
                    "Develop modern user interfaces and "
                    "component-based web applications."
                ),

                "skills": [
                    "javascript",
                    "react",
                    "responsive_design",
                    "api_integration",
                ],

                "prerequisites": [
                    "javascript",
                    "development_tools",
                ],

                "practice": [
                    "Learn component-based development.",
                    "Practice responsive layouts.",
                    "Consume APIs from frontend applications.",
                ],

                "project": (
                    "Build a modern frontend application using React."
                ),
            },

            {
                "stage_id": "backend_and_apis",

                "title": "Backend & APIs",

                "purpose": (
                    "Understand how web applications communicate "
                    "with servers and databases."
                ),

                "skills": [
                    "apis",
                    "backend_development",
                    "databases",
                    "sql",
                ],

                "prerequisites": [
                    "javascript",
                    "development_tools",
                ],

                "practice": [
                    "Understand HTTP and REST APIs.",
                    "Learn basic backend development.",
                    "Practice connecting applications to databases.",
                ],

                "project": (
                    "Build a full-stack web application with "
                    "an API and database."
                ),
            },

            {
                "stage_id": "portfolio",

                "title": "Web Development Portfolio",

                "purpose": (
                    "Demonstrate practical web-development ability "
                    "through real projects."
                ),

                "skills": [
                    "projects",
                    "github",
                    "communication",
                ],

                "prerequisites": [
                    "frontend_development",
                    "backend_and_apis",
                ],

                "practice": [
                    "Build 2–3 practical web applications.",
                    "Document your projects clearly.",
                    "Deploy projects online.",
                ],

                "project": (
                    "Build and deploy a portfolio containing "
                    "multiple web-development projects."
                ),
            },
        ],
    },

        "business_analyst": {

        "career_name": "Business Analyst",

        "domain": "Business & Management",

        "description": (
            "Uses business analysis, data, communication, "
            "and problem solving to improve decisions and processes."
        ),

        "stages": [

            {
                "stage_id": "business_foundations",
                "title": "Business Foundations",
                "purpose": (
                    "Understand how organizations, processes, "
                    "and business decisions work."
                ),
                "skills": [
                    "business_understanding",
                    "research",
                    "communication",
                ],
                "prerequisites": [],
                "practice": [
                    "Study basic business concepts.",
                    "Analyze simple business problems.",
                    "Practice documenting requirements.",
                ],
                "project": (
                    "Analyze a simple business process and suggest improvements."
                ),
            },

            {
                "stage_id": "data_analysis",
                "title": "Data & Analytical Skills",
                "purpose": (
                    "Develop the ability to analyze data "
                    "and extract useful business insights."
                ),
                "skills": [
                    "excel",
                    "sql",
                    "analytical_thinking",
                    "problem_solving",
                ],
                "prerequisites": [
                    "business_foundations",
                ],
                "practice": [
                    "Practice Excel analysis.",
                    "Learn basic SQL.",
                    "Analyze business datasets.",
                ],
                "project": (
                    "Create a business performance analysis dashboard."
                ),
            },

            {
                "stage_id": "requirements",
                "title": "Requirements & Process Analysis",
                "purpose": (
                    "Learn to understand stakeholder needs "
                    "and translate them into clear requirements."
                ),
                "skills": [
                    "requirements_analysis",
                    "documentation",
                    "communication",
                ],
                "prerequisites": [
                    "business_foundations",
                ],
                "practice": [
                    "Write functional requirements.",
                    "Create process diagrams.",
                    "Practice stakeholder interviews.",
                ],
                "project": (
                    "Create requirements documentation for a sample system."
                ),
            },

            {
                "stage_id": "communication",
                "title": "Communication & Presentation",
                "purpose": (
                    "Develop the ability to explain findings "
                    "and recommendations clearly."
                ),
                "skills": [
                    "communication",
                    "presentation",
                    "business_communication",
                ],
                "prerequisites": [
                    "requirements",
                    "data_analysis",
                ],
                "practice": [
                    "Present analytical findings.",
                    "Practice explaining technical ideas simply.",
                    "Create professional reports.",
                ],
                "project": (
                    "Present a complete business analysis case study."
                ),
            },

            {
                "stage_id": "portfolio",
                "title": "Business Analysis Portfolio",
                "purpose": (
                    "Demonstrate practical business-analysis ability."
                ),
                "skills": [
                    "projects",
                    "documentation",
                    "communication",
                ],
                "prerequisites": [
                    "communication",
                ],
                "practice": [
                    "Document business cases.",
                    "Create process analyses.",
                    "Publish projects and case studies.",
                ],
                "project": (
                    "Build 2–3 complete business-analysis case studies."
                ),
            },
        ],
    },


    "teacher": {

        "career_name": "Teacher / Educator",

        "domain": "Education",

        "description": (
            "Helps students learn, understand concepts, "
            "develop skills, and grow academically."
        ),

        "stages": [

            {
                "stage_id": "subject_foundations",
                "title": "Subject Knowledge",
                "purpose": (
                    "Build strong knowledge of the subject "
                    "you intend to teach."
                ),
                "skills": [
                    "subject_knowledge",
                    "research",
                ],
                "prerequisites": [],
                "practice": [
                    "Strengthen subject fundamentals.",
                    "Read reliable educational resources.",
                    "Practice explaining concepts.",
                ],
                "project": (
                    "Create a structured lesson on a subject topic."
                ),
            },

            {
                "stage_id": "teaching_foundations",
                "title": "Teaching Foundations",
                "purpose": (
                    "Understand how effective teaching "
                    "and learning work."
                ),
                "skills": [
                    "teaching",
                    "lesson_planning",
                    "assessment",
                ],
                "prerequisites": [
                    "subject_foundations",
                ],
                "practice": [
                    "Learn lesson-planning techniques.",
                    "Design learning objectives.",
                    "Create simple assessments.",
                ],
                "project": (
                    "Design a complete lesson plan."
                ),
            },

            {
                "stage_id": "communication",
                "title": "Communication & Presentation",
                "purpose": (
                    "Learn to explain ideas clearly and "
                    "engage different types of learners."
                ),
                "skills": [
                    "communication",
                    "presentation",
                    "empathy",
                ],
                "prerequisites": [
                    "teaching_foundations",
                ],
                "practice": [
                    "Practice explaining difficult concepts simply.",
                    "Develop presentation skills.",
                    "Practice active listening.",
                ],
                "project": (
                    "Deliver and record a short educational presentation."
                ),
            },

            {
                "stage_id": "classroom_management",
                "title": "Classroom Management",
                "purpose": (
                    "Develop skills for creating an effective "
                    "and supportive learning environment."
                ),
                "skills": [
                    "classroom_management",
                    "empathy",
                    "communication",
                ],
                "prerequisites": [
                    "communication",
                ],
                "practice": [
                    "Study classroom-management strategies.",
                    "Practice handling different classroom scenarios.",
                ],
                "project": (
                    "Create a classroom-management case study."
                ),
            },

            {
                "stage_id": "teaching_portfolio",
                "title": "Teaching Portfolio",
                "purpose": (
                    "Demonstrate teaching ability through "
                    "lessons, projects, and educational material."
                ),
                "skills": [
                    "teaching",
                    "lesson_planning",
                    "assessment",
                    "communication",
                ],
                "prerequisites": [
                    "classroom_management",
                ],
                "practice": [
                    "Create multiple lesson plans.",
                    "Build educational materials.",
                    "Document teaching projects.",
                ],
                "project": (
                    "Build a teaching portfolio with 3–5 lesson examples."
                ),
            },
        ],
    },
}


# ============================================================
# VALIDATION
# ============================================================

REQUIRED_ROADMAP_FIELDS = {
    "career_name",
    "domain",
    "description",
    "stages",
}


REQUIRED_STAGE_FIELDS = {
    "stage_id",
    "title",
    "purpose",
    "skills",
    "prerequisites",
    "practice",
    "project",
}


def validate_roadmap_data():
    """
    Validate the roadmap knowledge base.

    Raises ValueError if the structure is invalid.
    """

    if not isinstance(
        ROADMAPS,
        dict,
    ):
        raise ValueError(
            "ROADMAPS must be a dictionary."
        )

    if not ROADMAPS:

        raise ValueError(
            "ROADMAPS cannot be empty."
        )

    stage_ids_by_career = {}

    for career_id, roadmap in ROADMAPS.items():

        # ----------------------------------------------------
        # Career structure
        # ----------------------------------------------------

        missing_fields = (
            REQUIRED_ROADMAP_FIELDS
            - set(roadmap.keys())
        )

        if missing_fields:

            raise ValueError(
                f"Career '{career_id}' is missing "
                f"fields: {sorted(missing_fields)}"
            )

        if not roadmap[
            "stages"
        ]:

            raise ValueError(
                f"Career '{career_id}' "
                "must contain at least one stage."
            )

        # ----------------------------------------------------
        # Stage IDs
        # ----------------------------------------------------

        stage_ids = set()

        for stage in roadmap[
            "stages"
        ]:

            missing_stage_fields = (
                REQUIRED_STAGE_FIELDS
                - set(stage.keys())
            )

            if missing_stage_fields:

                raise ValueError(
                    f"Career '{career_id}' has a stage "
                    f"missing fields: "
                    f"{sorted(missing_stage_fields)}"
                )

            stage_id = stage[
                "stage_id"
            ]

            if stage_id in stage_ids:

                raise ValueError(
                    f"Career '{career_id}' contains "
                    f"duplicate stage ID: "
                    f"{stage_id}"
                )

            stage_ids.add(
                stage_id
            )

            # ------------------------------------------------
            # Validate lists
            # ------------------------------------------------

            if not isinstance(
                stage["skills"],
                list,
            ):

                raise ValueError(
                    f"Stage '{stage_id}' in "
                    f"'{career_id}' must have "
                    f"a skills list."
                )

            if not isinstance(
                stage["prerequisites"],
                list,
            ):

                raise ValueError(
                    f"Stage '{stage_id}' in "
                    f"'{career_id}' must have "
                    f"a prerequisites list."
                )

            if not isinstance(
                stage["practice"],
                list,
            ):

                raise ValueError(
                    f"Stage '{stage_id}' in "
                    f"'{career_id}' must have "
                    f"a practice list."
                )

            if not isinstance(
                stage["project"],
                str,
            ):

                raise ValueError(
                    f"Stage '{stage_id}' in "
                    f"'{career_id}' must have "
                    f"a project description."
                )

        stage_ids_by_career[
            career_id
        ] = stage_ids

    # ========================================================
    # Validate prerequisites
    # ========================================================

    for career_id, roadmap in ROADMAPS.items():

        valid_stage_ids = (
            stage_ids_by_career[
                career_id
            ]
        )

        for stage in roadmap[
            "stages"
        ]:

            for prerequisite in stage[
                "prerequisites"
            ]:

                if prerequisite not in valid_stage_ids:

                    raise ValueError(
                        f"Career '{career_id}', "
                        f"stage '{stage['stage_id']}' "
                        f"references unknown prerequisite "
                        f"'{prerequisite}'."
                    )

    return True


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_roadmap(
    career_id,
):
    """
    Return the roadmap for a career.
    """

    if career_id not in ROADMAPS:

        raise ValueError(
            f"Unknown career ID: "
            f"{career_id}"
        )

    return ROADMAPS[
        career_id
    ]


def get_stage(
    career_id,
    stage_id,
):
    """
    Return one stage from a career roadmap.
    """

    roadmap = get_roadmap(
        career_id
    )

    for stage in roadmap[
        "stages"
    ]:

        if stage[
            "stage_id"
        ] == stage_id:

            return stage

    raise ValueError(
        f"Unknown stage '{stage_id}' "
        f"for career '{career_id}'."
    )


def get_career_ids():
    """
    Return all supported roadmap career IDs.
    """

    return list(
        ROADMAPS.keys()
    )


# ============================================================
# MAIN VALIDATION
# ============================================================

if __name__ == "__main__":

    validate_roadmap_data()

    print(
        "Roadmap knowledge base validation successful."
    )

    print(
        f"Number of career roadmaps: "
        f"{len(ROADMAPS)}"
    )

    for career_id, roadmap in (
        ROADMAPS.items()
    ):

        print(
            f"- {roadmap['career_name']} "
            f"({len(roadmap['stages'])} stages)"
        )

    print()

    print(
        "All roadmap structures and prerequisites "
        "are valid."
    )