"""
Career Explanation Engine
-------------------------

Converts numerical career-matching results into
student-friendly and supportive explanations.

This module explains:

    1. Why a career may suit the student
    2. Strong matching areas
    3. Growth opportunities
    4. Priority growth areas
    5. Evidence/confidence
    6. Core skills
    7. Education/pathway information
    8. Current skill strengths
    9. Skill gaps
    10. Skills requiring more information
    11. Personalized roadmap

IMPORTANT:

This module does NOT decide a student's career.

It provides guidance based on the results produced
by the Career Matching Engine, Skill-Gap Engine,
and Roadmap Personalization Engine.
"""


# ============================================================
# IMPORTS
# ============================================================

from career_matching import (
    build_test_student_profiles,
    get_top_career_recommendations,
)

from skill_gap import (
    calculate_skill_gap,
)

from student_skills import (
    create_student_skill_profile,
)

from roadmap import (
    generate_personalized_roadmap,
)


# ============================================================
# DISPLAY NAMES
# ============================================================

DIMENSION_DISPLAY_NAMES = {

    # --------------------------------------------------------
    # Interest
    # --------------------------------------------------------

    "technology": "Technology",
    "mathematics": "Mathematics",
    "science": "Science",
    "biology_health": "Biology & Health",
    "business": "Business",
    "finance": "Finance",
    "law": "Law & Justice",
    "social_issues": "Social Issues",
    "public_service": "Public Service",
    "communication": "Communication",
    "creative_arts": "Creative Arts",
    "media": "Media",
    "people_helping": "Helping People",
    "research": "Research",
    "nature_environment": "Nature & Environment",
    "physical_activity": "Physical Activity",

    # --------------------------------------------------------
    # Aptitude
    # --------------------------------------------------------

    "logical_reasoning": "Logical Reasoning",
    "numerical_ability": "Numerical Ability",
    "analytical_thinking": "Analytical Thinking",
    "problem_solving": "Problem Solving",
    "verbal_ability": "Verbal Ability",
    "spatial_reasoning": "Spatial Reasoning",
    "creative_thinking": "Creative Thinking",
    "attention_detail": "Attention to Detail",

    # --------------------------------------------------------
    # Work Style
    # --------------------------------------------------------

    "people_interaction": "People Interaction",
    "helping_others": "Helping Others",
    "teamwork": "Teamwork",
    "independent_work": "Independent Work",
    "leadership": "Leadership",
    "data_work": "Data-Oriented Work",
    "technology_work": "Technology-Oriented Work",
    "creative_work": "Creative Work",
    "research_work": "Research-Oriented Work",
    "field_work": "Field Work",
    "structured_work": "Structured Work",
    "flexible_work": "Flexible Work",
}


# ============================================================
# RECOMMENDATION MESSAGES
# ============================================================

RECOMMENDATION_MESSAGES = {

    "Strong Match": (
        "This career direction shows strong alignment "
        "with your current interests, abilities, and "
        "preferred way of working."
    ),

    "Good Match": (
        "This career direction shows good alignment "
        "with your current profile and is worth exploring "
        "further."
    ),

    "Moderate Match": (
        "This career direction has some meaningful "
        "alignment with your profile. Exploring the field "
        "further can help you decide whether it feels right."
    ),

    "Explore Further": (
        "Some parts of this career direction align with "
        "your profile, but more exploration is recommended "
        "before making a decision."
    ),

    "Low Alignment": (
        "Your current profile shows limited alignment with "
        "this career direction. This does not mean you "
        "cannot pursue it; it simply suggests exploring "
        "other directions as well."
    ),
}


# ============================================================
# STRENGTH PHRASES
# ============================================================

STRENGTH_PHRASES = {

    "Interest": {

        "technology": (
            "You show strong interest in technology."
        ),

        "mathematics": (
            "You show strong interest in mathematics."
        ),

        "science": (
            "You show strong interest in science."
        ),

        "biology_health": (
            "You show strong interest in biology and health."
        ),

        "business": (
            "You show interest in business and commercial "
            "problem solving."
        ),

        "finance": (
            "You show interest in finance and financial topics."
        ),

        "law": (
            "You show strong interest in law and justice."
        ),

        "social_issues": (
            "You show interest in social issues and society."
        ),

        "public_service": (
            "You show interest in public service."
        ),

        "communication": (
            "Communication appears to be one of your "
            "stronger interests."
        ),

        "creative_arts": (
            "You show interest in creative and artistic work."
        ),

        "media": (
            "You show interest in media and communication."
        ),

        "people_helping": (
            "You show a strong interest in helping people."
        ),

        "research": (
            "You show strong interest in research and "
            "investigation."
        ),

        "nature_environment": (
            "You show interest in nature and environmental topics."
        ),

        "physical_activity": (
            "You show interest in physical activity."
        ),
    },

    "Aptitude": {

        "logical_reasoning": (
            "Your logical reasoning appears to be a strength."
        ),

        "numerical_ability": (
            "Your numerical ability is a strong area."
        ),

        "analytical_thinking": (
            "Your analytical thinking appears to be strong."
        ),

        "problem_solving": (
            "Problem solving is one of your stronger abilities."
        ),

        "verbal_ability": (
            "Your verbal ability is a strong area."
        ),

        "spatial_reasoning": (
            "You show strength in spatial reasoning."
        ),

        "creative_thinking": (
            "Your creative thinking appears to be a strength."
        ),

        "attention_detail": (
            "Your attention to detail is a strong area."
        ),
    },

    "Work Style": {

        "people_interaction": (
            "You appear comfortable with people-oriented work."
        ),

        "helping_others": (
            "You show a preference for helping others through "
            "your work."
        ),

        "teamwork": (
            "You appear comfortable working as part of a team."
        ),

        "independent_work": (
            "You show a preference for independent work."
        ),

        "leadership": (
            "You show some preference for leadership and "
            "responsibility."
        ),

        "data_work": (
            "You appear comfortable working with data."
        ),

        "technology_work": (
            "You show a strong preference for "
            "technology-oriented work."
        ),

        "creative_work": (
            "You show a strong preference for creative work."
        ),

        "research_work": (
            "You appear comfortable with research-oriented work."
        ),

        "field_work": (
            "You show some preference for practical or "
            "field-based work."
        ),

        "structured_work": (
            "You appear comfortable with structured work."
        ),

        "flexible_work": (
            "You show a preference for flexible working "
            "environments."
        ),
    },
}


# ============================================================
# GROWTH PHRASES
# ============================================================

GROWTH_PHRASES = {

    "Interest": {

        "technology": (
            "Increasing your exposure to technology through "
            "small projects or exploration could strengthen "
            "your preparation."
        ),

        "mathematics": (
            "Building further comfort with mathematics could "
            "strengthen your preparation for this direction."
        ),

        "science": (
            "Exploring science-related topics more deeply could "
            "strengthen your preparation."
        ),

        "biology_health": (
            "Exploring biology and health-related subjects could "
            "help you understand this direction better."
        ),

        "business": (
            "Exploring business concepts and real-world business "
            "problems could strengthen your preparation."
        ),

        "finance": (
            "Developing your understanding of finance could "
            "strengthen your preparation."
        ),

        "law": (
            "Exploring legal concepts, current affairs, and "
            "real-world cases could strengthen your understanding."
        ),

        "social_issues": (
            "Engaging more with social issues could help you "
            "understand this career direction."
        ),

        "public_service": (
            "Exploring public-service topics and current affairs "
            "could strengthen your understanding."
        ),

        "communication": (
            "Developing communication skills through writing, "
            "presentations, or discussions could be useful."
        ),

        "creative_arts": (
            "Building more creative practice could strengthen "
            "your preparation."
        ),

        "media": (
            "Exploring media and communication projects could "
            "help you understand this direction."
        ),

        "people_helping": (
            "More exposure to people-oriented activities could "
            "help you explore this field."
        ),

        "research": (
            "Developing research habits and gaining practical "
            "research experience could strengthen your preparation."
        ),

        "nature_environment": (
            "Exploring environmental topics and practical "
            "activities could help you understand this direction."
        ),

        "physical_activity": (
            "Increasing exposure to practical or physical "
            "activities could help you explore this direction."
        ),
    },

    "Aptitude": {

        "logical_reasoning": (
            "Practice logical reasoning through structured "
            "problem-solving exercises."
        ),

        "numerical_ability": (
            "Strengthen numerical ability through mathematics, "
            "statistics, and quantitative practice."
        ),

        "analytical_thinking": (
            "Practice breaking complex problems into smaller "
            "parts and comparing possible solutions."
        ),

        "problem_solving": (
            "Work on progressively harder real-world and "
            "technical problems."
        ),

        "verbal_ability": (
            "Practice reading, writing, explanation, and "
            "structured communication."
        ),

        "spatial_reasoning": (
            "Practice visualisation, diagrams, and spatial "
            "reasoning exercises."
        ),

        "creative_thinking": (
            "Work on open-ended problems where multiple "
            "solutions are possible."
        ),

        "attention_detail": (
            "Practice careful checking, documentation, and "
            "error detection."
        ),
    },

    "Work Style": {

        "people_interaction": (
            "Get more exposure to activities involving "
            "communication and interaction with people."
        ),

        "helping_others": (
            "Participate in mentoring, volunteering, or "
            "other activities where you help others."
        ),

        "teamwork": (
            "Participate in team projects to strengthen "
            "collaboration."
        ),

        "independent_work": (
            "Try small self-directed projects that require "
            "you to plan and complete tasks independently."
        ),

        "leadership": (
            "Take responsibility for small projects, events, "
            "or team activities."
        ),

        "data_work": (
            "Practice working with datasets, tables, charts, "
            "and basic data analysis."
        ),

        "technology_work": (
            "Build small technology projects to gain practical "
            "experience."
        ),

        "creative_work": (
            "Build a portfolio of creative work and experiment "
            "with different forms of design."
        ),

        "research_work": (
            "Practice researching a topic, comparing sources, "
            "and presenting your findings."
        ),

        "field_work": (
            "Try practical activities, field visits, or "
            "hands-on experiences where possible."
        ),

        "structured_work": (
            "Practice following structured plans and "
            "completing tasks consistently."
        ),

        "flexible_work": (
            "Try projects where requirements are open-ended "
            "and you need to adapt as you work."
        ),
    },
}


# ============================================================
# MATCH INTERPRETATION
# ============================================================

def get_match_strength(
    student_score,
    career_requirement,
):
    """
    Compare the student's score with the career requirement.

    Returns:

        strong
        good
        growth
        priority
    """

    if career_requirement <= 0:

        return "not_relevant"

    ratio = (
        student_score
        / career_requirement
    )

    if ratio >= 0.90:

        return "strong"

    if ratio >= 0.75:

        return "good"

    if ratio >= 0.50:

        return "growth"

    return "priority"


# ============================================================
# GENERATE STRENGTH EXPLANATIONS
# ============================================================

def generate_strength_explanations(
    result,
    max_items=3,
):
    """
    Generate explanations for the strongest
    career-relevant dimensions.
    """

    explanations = []

    for item in result[
        "strongest_dimensions"
    ]:

        if len(explanations) >= max_items:

            break

        dimension = item[
            "dimension"
        ]

        category = item[
            "category"
        ]

        student_score = item[
            "student_score"
        ]

        career_requirement = item[
            "career_requirement"
        ]

        strength = get_match_strength(
            student_score,
            career_requirement,
        )

        if strength not in (
            "strong",
            "good",
        ):

            continue

        category_phrases = (
            STRENGTH_PHRASES.get(
                category,
                {},
            )
        )

        phrase = category_phrases.get(
            dimension
        )

        if phrase is None:

            display_name = (
                DIMENSION_DISPLAY_NAMES.get(
                    dimension,
                    dimension,
                )
            )

            phrase = (
                f"Your {display_name.lower()} "
                "shows good alignment with this "
                "career direction."
            )

        explanations.append(
            {
                "category": category,

                "dimension": dimension,

                "display_name": (
                    DIMENSION_DISPLAY_NAMES.get(
                        dimension,
                        dimension,
                    )
                ),

                "student_score": round(
                    student_score,
                    2,
                ),

                "career_requirement": round(
                    career_requirement,
                    2,
                ),

                "text": phrase,
            }
        )

    return explanations


# ============================================================
# GENERATE GROWTH OPPORTUNITIES
# ============================================================

def generate_growth_opportunities(
    result,
    max_items=3,
):
    """
    Identify dimensions where development could strengthen
    the student's preparation for the career.

    A lower score is NOT described as failure.
    """

    opportunities = []

    for item in result[
        "development_areas"
    ]:

        if len(opportunities) >= max_items:

            break

        dimension = item[
            "dimension"
        ]

        category = item[
            "category"
        ]

        student_score = item[
            "student_score"
        ]

        career_requirement = item[
            "career_requirement"
        ]

        gap = item[
            "gap"
        ]

        classification = get_match_strength(
            student_score,
            career_requirement,
        )

        if classification not in (
            "growth",
            "priority",
        ):

            continue

        category_phrases = (
            GROWTH_PHRASES.get(
                category,
                {},
            )
        )

        phrase = category_phrases.get(
            dimension
        )

        if phrase is None:

            display_name = (
                DIMENSION_DISPLAY_NAMES.get(
                    dimension,
                    dimension,
                )
            )

            phrase = (
                f"Developing your "
                f"{display_name.lower()} "
                "could strengthen your preparation "
                "for this career direction."
            )

        opportunities.append(
            {
                "category": category,

                "dimension": dimension,

                "display_name": (
                    DIMENSION_DISPLAY_NAMES.get(
                        dimension,
                        dimension,
                    )
                ),

                "student_score": round(
                    student_score,
                    2,
                ),

                "career_requirement": round(
                    career_requirement,
                    2,
                ),

                "gap": round(
                    gap,
                    2,
                ),

                "priority": (
                    "High"
                    if classification == "priority"
                    else "Medium"
                ),

                "text": phrase,
            }
        )

    return opportunities


# ============================================================
# EVIDENCE MESSAGE
# ============================================================

def generate_evidence_message(
    evidence_coverage,
):
    """
    Convert evidence coverage into a student-friendly
    message.
    """

    if evidence_coverage >= 85:

        return (
            "Your profile has strong evidence across the "
            "areas used for this recommendation."
        )

    if evidence_coverage >= 65:

        return (
            "Your profile has reasonably good evidence, "
            "although some areas could be explored further."
        )

    if evidence_coverage >= 40:

        return (
            "The recommendation is based on partial evidence. "
            "More information about your interests and "
            "preferences could improve the match."
        )

    return (
        "This recommendation currently has limited evidence. "
        "Treat it as an option to explore rather than a strong "
        "conclusion."
    )


# ============================================================
# CAREER SUMMARY
# ============================================================

def generate_career_summary(
    result,
):
    """
    Generate the main explanation paragraph.
    """

    career_name = result[
        "career_name"
    ]

    recommendation = result[
        "recommendation"
    ]

    match_score = result[
        "overall_match"
    ]

    base_message = (
        RECOMMENDATION_MESSAGES.get(
            recommendation,
            "This career direction is worth exploring "
            "based on your current profile.",
        )
    )

    return (
        f"{career_name} has a current match score of "
        f"{match_score:.1f}%. "
        f"{base_message}"
    )


# ============================================================
# SKILL GAP EXPLANATION
# ============================================================

def generate_skill_gap_explanation(
    result,
    student_skill_profile=None,
):
    """
    Generate the skill-gap portion of a career explanation.

    If no student skill profile is supplied, the career
    explanation still works, but skill-gap analysis is not
    generated.
    """

    if student_skill_profile is None:

        return None

    return calculate_skill_gap(
        result[
            "career_id"
        ],
        student_skill_profile,
    )


# ============================================================
# SKILL SUMMARY
# ============================================================

def build_skill_summary(
    skill_gap_report,
):
    """
    Convert the raw skill-gap report into a compact
    explanation structure.
    """

    if skill_gap_report is None:

        return None

    return {

        "readiness": skill_gap_report[
            "overall_skill_readiness"
        ],

        "evidence_coverage": skill_gap_report[
            "skill_evidence_coverage"
        ],

        "current_strengths": (
            skill_gap_report[
                "current_strengths"
            ]
        ),

        "growth_opportunities": (
            skill_gap_report[
                "growth_opportunities"
            ]
        ),

        "high_priority_gaps": (
            skill_gap_report[
                "high_priority_gaps"
            ]
        ),

        "medium_priority_gaps": (
            skill_gap_report[
                "medium_priority_gaps"
            ]
        ),

        "low_priority_gaps": (
            skill_gap_report[
                "low_priority_gaps"
            ]
        ),

        "needs_more_information": (
            skill_gap_report[
                "needs_more_information"
            ]
        ),
    }


# ============================================================
# ROADMAP EXPLANATION
# ============================================================

def generate_roadmap_explanation(
    result,
    student_skill_profile=None,
):
    """
    Generate a personalized roadmap for the selected career.

    The roadmap is optional so the Career Explanation Engine
    remains usable even when a skill profile is unavailable.
    """

    if student_skill_profile is None:

        return None

    return generate_personalized_roadmap(
        result[
            "career_id"
        ],
        student_skill_profile,
    )


# ============================================================
# COMPLETE CAREER EXPLANATION
# ============================================================

def generate_career_explanation(
    result,
    student_skill_profile=None,
    max_strengths=3,
    max_growth_opportunities=3,
):
    """
    Convert a career matching result into a complete,
    UI-ready explanation object.

    Includes:

        Career explanation
        Skill gap
        Personalized roadmap
    """

    strengths = (
        generate_strength_explanations(
            result,
            max_items=max_strengths,
        )
    )

    growth_opportunities = (
        generate_growth_opportunities(
            result,
            max_items=max_growth_opportunities,
        )
    )

    evidence_message = (
        generate_evidence_message(
            result[
                "evidence_coverage"
            ]
        )
    )

    summary = (
        generate_career_summary(
            result
        )
    )

    skill_gap_report = (
        generate_skill_gap_explanation(
            result,
            student_skill_profile,
        )
    )

    skill_summary = (
        build_skill_summary(
            skill_gap_report
        )
    )

    roadmap = (
        generate_roadmap_explanation(
            result,
            student_skill_profile,
        )
    )

    return {

        "career_id": result[
            "career_id"
        ],

        "career_name": result[
            "career_name"
        ],

        "domain": result[
            "domain"
        ],

        "match_score": result[
            "overall_match"
        ],

        "recommendation": result[
            "recommendation"
        ],

        "summary": summary,

        "why_this_may_suit_you": strengths,

        "growth_opportunities": (
            growth_opportunities
        ),

        "evidence_message": evidence_message,

        "core_skills": result[
            "core_skills"
        ],

        "education_notes": result[
            "education_notes"
        ],

        # ----------------------------------------------------
        # Skill-gap information
        # ----------------------------------------------------

        "skill_gap": skill_summary,

        # ----------------------------------------------------
        # Personalized roadmap
        # ----------------------------------------------------

        "roadmap": roadmap,
    }


# ============================================================
# EXPLAIN TOP CAREER RECOMMENDATIONS
# ============================================================

def explain_top_career_recommendations(
    interest_profile,
    aptitude_profile,
    work_style_profile,
    top_n=3,
    student_skill_profile=None,
):
    """
    Match a student against careers and generate
    explanations for the top recommendations.
    """

    results = get_top_career_recommendations(
        interest_profile,
        aptitude_profile,
        work_style_profile,
        top_n=top_n,
    )

    explanations = []

    for result in results:

        explanation = (
            generate_career_explanation(
                result,
                student_skill_profile=(
                    student_skill_profile
                ),
            )
        )

        explanations.append(
            explanation
        )

    return explanations


# ============================================================
# PRINT SKILL GAP SECTION
# ============================================================

def print_skill_gap_section(
    skill_gap,
):
    """
    Print skill-gap information in a readable format.
    """

    if skill_gap is None:

        print(
            "Skill-gap analysis:"
        )

        print(
            "  - No student skill profile was supplied."
        )

        return

    print()

    print(
        "Skill readiness:"
    )

    print(
        f"  {skill_gap['readiness']:.1f}%"
    )

    print(
        f"Skill evidence coverage: "
        f"{skill_gap['evidence_coverage']:.1f}%"
    )

    # --------------------------------------------------------
    # Current strengths
    # --------------------------------------------------------

    print()

    print(
        "Current skill strengths:"
    )

    strengths = skill_gap[
        "current_strengths"
    ]

    if not strengths:

        print(
            "  - None identified yet."
        )

    else:

        for item in strengths:

            skill_name = (
                item["skill_id"]
                .replace("_", " ")
                .title()
            )

            print(
                f"  - {skill_name}: "
                f"{item['current_level']}"
            )

    # --------------------------------------------------------
    # High priority
    # --------------------------------------------------------

    print()

    print(
        "High-priority skill gaps:"
    )

    high_priority = skill_gap[
        "high_priority_gaps"
    ]

    if not high_priority:

        print(
            "  - None identified."
        )

    else:

        for item in high_priority:

            skill_name = (
                item["skill_id"]
                .replace("_", " ")
                .title()
            )

            print(
                f"  - {skill_name}: "
                f"{item['current_level']} "
                f"-> "
                f"{item['expected_level']}"
            )

    # --------------------------------------------------------
    # Medium priority
    # --------------------------------------------------------

    print()

    print(
        "Medium-priority skill gaps:"
    )

    medium_priority = skill_gap[
        "medium_priority_gaps"
    ]

    if not medium_priority:

        print(
            "  - None identified."
        )

    else:

        for item in medium_priority:

            skill_name = (
                item["skill_id"]
                .replace("_", " ")
                .title()
            )

            print(
                f"  - {skill_name}: "
                f"{item['current_level']} "
                f"-> "
                f"{item['expected_level']}"
            )

    # --------------------------------------------------------
    # Unknown
    # --------------------------------------------------------

    print()

    print(
        "Skills needing more information:"
    )

    unknown = skill_gap[
        "needs_more_information"
    ]

    if not unknown:

        print(
            "  - None."
        )

    else:

        for item in unknown:

            skill_name = (
                item["skill_id"]
                .replace("_", " ")
                .title()
            )

            print(
                f"  - {skill_name}"
            )


# ============================================================
# PRINT ROADMAP SECTION
# ============================================================

def print_roadmap_section(
    roadmap,
):
    """
    Print the most useful roadmap information.

    The complete roadmap remains available in the returned
    data structure, but the terminal output focuses on:

        Start Now
        Next
        Later
    """

    if roadmap is None:

        return

    print()

    print(
        "----------------------------------------"
    )

    print(
        "PERSONALIZED ROADMAP"
    )

    print(
        "----------------------------------------"
    )

    # --------------------------------------------------------
    # Start Now
    # --------------------------------------------------------

    print()

    print(
        "🎯 START NOW"
    )

    starting_stage = roadmap[
        "starting_stage"
    ]

    if starting_stage is None:

        print(
            "  - No incomplete starting stage identified."
        )

    else:

        print(
            f"  → {starting_stage['title']}"
        )

        print(
            f"    {starting_stage['summary']}"
        )

        if starting_stage[
            "practice"
        ]:

            print(
                f"    First action: "
                f"{starting_stage['practice'][0]}"
            )

    # --------------------------------------------------------
    # Next
    # --------------------------------------------------------

    print()

    print(
        "➡️ NEXT"
    )

    next_stage = roadmap[
        "next_stage"
    ]

    if next_stage is None:

        print(
            "  - No next stage currently identified."
        )

    else:

        print(
            f"  → {next_stage['title']}"
        )

    # --------------------------------------------------------
    # Later
    # --------------------------------------------------------

    print()

    print(
        "🔭 LATER"
    )

    later_stages = roadmap[
        "later_stages"
    ]

    if not later_stages:

        print(
            "  - No additional incomplete stages."
        )

    else:

        for stage in later_stages:

            print(
                f"  - {stage['title']}"
            )


# ============================================================
# PRINT COMPLETE EXPLANATION
# ============================================================

def print_career_explanation(
    explanation,
    rank=None,
):
    """
    Print a readable explanation for terminal testing.
    """

    print()

    print(
        "=" * 80
    )

    if rank is not None:

        print(
            f"{rank}. "
            f"{explanation['career_name']}"
        )

    else:

        print(
            explanation[
                "career_name"
            ]
        )

    print(
        "=" * 80
    )

    print(
        f"Domain: "
        f"{explanation['domain']}"
    )

    print(
        f"Match: "
        f"{explanation['match_score']:.1f}%"
    )

    print(
        f"Recommendation: "
        f"{explanation['recommendation']}"
    )

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    print()

    print(
        "Summary:"
    )

    print(
        explanation[
            "summary"
        ]
    )

    # --------------------------------------------------------
    # Strengths
    # --------------------------------------------------------

    print()

    print(
        "Why this may suit you:"
    )

    strengths = explanation[
        "why_this_may_suit_you"
    ]

    if not strengths:

        print(
            "  - No strong matching area "
            "was identified from the current evidence."
        )

    else:

        for item in strengths:

            print(
                f"  - {item['text']}"
            )

    # --------------------------------------------------------
    # Growth opportunities
    # --------------------------------------------------------

    print()

    print(
        "Profile development opportunities:"
    )

    growth_opportunities = explanation[
        "growth_opportunities"
    ]

    if not growth_opportunities:

        print(
            "  - No major development opportunity "
            "was identified from the current profile."
        )

    else:

        for item in growth_opportunities:

            print(
                f"  - [{item['priority']}] "
                f"{item['text']}"
            )

    # --------------------------------------------------------
    # Evidence
    # --------------------------------------------------------

    print()

    print(
        "Profile evidence:"
    )

    print(
        f"  {explanation['evidence_message']}"
    )

    # --------------------------------------------------------
    # Core skills
    # --------------------------------------------------------

    print()

    print(
        "Core skills:"
    )

    for skill in explanation[
        "core_skills"
    ]:

        print(
            f"  - {skill}"
        )

    # --------------------------------------------------------
    # Education
    # --------------------------------------------------------

    print()

    print(
        "Education / pathway note:"
    )

    print(
        f"  {explanation['education_notes']}"
    )

    # --------------------------------------------------------
    # Skill Gap
    # --------------------------------------------------------

    print()

    print(
        "----------------------------------------"
    )

    print(
        "SKILL DEVELOPMENT"
    )

    print(
        "----------------------------------------"
    )

    print_skill_gap_section(
        explanation[
            "skill_gap"
        ]
    )

    # --------------------------------------------------------
    # Roadmap
    # --------------------------------------------------------

    print_roadmap_section(
        explanation[
            "roadmap"
        ]
    )


# ============================================================
# TEST SKILL PROFILES
# ============================================================

def build_test_skill_profiles():
    """
    Build the skill profiles used for terminal testing.

    These are based on the same test students used by
    the Skill-Gap Engine.

    They are NOT final application inputs.
    """

    from skill_gap import (
        STUDENT_A_SKILLS,
        STUDENT_B_SKILLS,
    )

    student_a_skill_profile = (
        create_student_skill_profile(
            "college",
            STUDENT_A_SKILLS,
        )
    )

    student_b_skill_profile = (
        create_student_skill_profile(
            "school",
            STUDENT_B_SKILLS,
        )
    )

    return (
        student_a_skill_profile,
        student_b_skill_profile,
    )


# ============================================================
# MAIN TEST
# ============================================================

if __name__ == "__main__":

    print(
        "Career Explanation Engine"
    )

    print(
        "=" * 80
    )

    # --------------------------------------------------------
    # Build matching test students.
    # --------------------------------------------------------

    student_a, student_b = (
        build_test_student_profiles()
    )

    # --------------------------------------------------------
    # Build skill test profiles.
    # --------------------------------------------------------

    (
        student_a_skills,
        student_b_skills,
    ) = build_test_skill_profiles()

    # ========================================================
    # STUDENT A
    # ========================================================

    print()

    print(
        "STUDENT A"
    )

    print(
        "=" * 80
    )

    student_a_explanations = (
        explain_top_career_recommendations(
            student_a["interest"],
            student_a["aptitude"],
            student_a["work_style"],
            top_n=3,
            student_skill_profile=(
                student_a_skills
            ),
        )
    )

    for index, explanation in enumerate(
        student_a_explanations,
        start=1,
    ):

        print_career_explanation(
            explanation,
            rank=index,
        )

    # ========================================================
    # STUDENT B
    # ========================================================

    print()

    print(
        "STUDENT B"
    )

    print(
        "=" * 80
    )

    student_b_explanations = (
        explain_top_career_recommendations(
            student_b["interest"],
            student_b["aptitude"],
            student_b["work_style"],
            top_n=3,
            student_skill_profile=(
                student_b_skills
            ),
        )
    )

    for index, explanation in enumerate(
        student_b_explanations,
        start=1,
    ):

        print_career_explanation(
            explanation,
            rank=index,
        )

    # ========================================================
    # FINAL STATUS
    # ========================================================

    print()

    print(
        "=" * 80
    )

    print(
        "Career explanation test completed successfully."
    )

    print(
        "Career matching, skill-gap analysis, and "
        "personalized roadmap are now integrated."
    )

    print(
        "The system provides guidance and development "
        "opportunities rather than determining a student's career."
    )