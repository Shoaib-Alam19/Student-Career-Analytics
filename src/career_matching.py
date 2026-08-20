"""
Career Matching Engine
----------------------

Compares a student's:

    1. Interest profile
    2. Aptitude profile
    3. Work-style profile

against structured career profiles.

IMPORTANT:
    This engine provides career directions to explore.
    It does NOT determine a student's destiny.

Match score:
    Interest   -> 40%
    Aptitude   -> 35%
    Work Style -> 25%

Each individual dimension is weighted according to how
relevant that dimension is to the career.

The engine also produces:

    - overall match score
    - component scores
    - evidence coverage
    - strongest matching dimensions
    - development areas
    - recommendation strength
"""


# ============================================================
# IMPORT CAREER DATA
# ============================================================

from career_data import (
    CAREER_PROFILES,
    validate_career_profiles,
)


# ============================================================
# MATCHING WEIGHTS
# ============================================================

MATCHING_WEIGHTS = {
    "interest": 0.40,
    "aptitude": 0.35,
    "work_style": 0.25,
}




# ============================================================
# EDUCATION BOOSTS
# ============================================================

EDUCATION_BOOSTS = {
    "School": {"doctor","lawyer","teacher","graphic_designer","civil_services_officer","research_scientist"},
    "College": {"software_developer","web_developer","data_analyst","data_scientist","ai_ml_engineer","cybersecurity_analyst","business_analyst","entrepreneur"},
    "Graduate": {"cloud_engineer","devops_engineer","financial_analyst","research_scientist","cybersecurity_analyst"},
}

def apply_education_boost(score, career_id, education_level):
    if not education_level:
        return score
    careers=EDUCATION_BOOSTS.get(education_level,set())
    if career_id in careers:
        score=min(100, score*1.06)
    return round(score,2)

# ============================================================
# VALIDATION
# ============================================================

def validate_matching_weights():
    """
    Make sure the major matching weights add up to 1.
    """

    total = sum(
        MATCHING_WEIGHTS.values()
    )

    if abs(total - 1.0) > 0.000001:
        raise ValueError(
            "Matching weights must add up to 1.0."
        )

    return True


# ============================================================
# DIMENSION SCORE
# ============================================================

def calculate_dimension_match(
    student_scores,
    career_requirements,
):
    """
    Calculate how well a student's scores align with
    the dimensions that matter for a career.

    Formula:

        sum(student_score × career_requirement)
        ---------------------------------------
             sum(career_requirement)

    Student score:
        0-10

    Career requirement:
        0-10

    Result:
        0-100
    """

    weighted_score = 0.0
    total_relevance = 0.0

    for dimension, requirement in (
        career_requirements.items()
    ):

        # A requirement of 0 means that this dimension
        # does not influence the career component.

        if requirement <= 0:
            continue

        student_score = student_scores.get(
            dimension,
            0.0,
        )

        weighted_score += (
            student_score
            * requirement
        )

        total_relevance += requirement

    if total_relevance == 0:
        return 0.0

    score = (
        weighted_score
        / total_relevance
    )

    return round(
        score * 10,
        2,
    )


# ============================================================
# DIMENSION CONTRIBUTIONS
# ============================================================

def calculate_dimension_contributions(
    student_scores,
    career_requirements,
):
    """
    Calculate the contribution of each relevant dimension.

    This is used later to explain WHY a career matches.
    """

    contributions = []

    total_relevance = sum(
        requirement
        for requirement in career_requirements.values()
        if requirement > 0
    )

    if total_relevance == 0:
        return contributions

    for dimension, requirement in (
        career_requirements.items()
    ):

        if requirement <= 0:
            continue

        student_score = student_scores.get(
            dimension,
            0.0,
        )

        contribution = (
            student_score
            * requirement
            / total_relevance
        ) * 10

        contributions.append(
            {
                "dimension": dimension,
                "student_score": round(
                    student_score,
                    2,
                ),
                "career_requirement": round(
                    requirement,
                    2,
                ),
                "contribution": round(
                    contribution,
                    2,
                ),
            }
        )

    return contributions


# ============================================================
# EVIDENCE COVERAGE
# ============================================================

def calculate_component_evidence_coverage(
    student_scores,
    evidence_coverage,
    career_requirements,
):
    """
    Calculate evidence coverage for the dimensions that
    actually matter to a career.

    Career-relevant dimensions have greater influence
    on the coverage value.
    """

    weighted_coverage = 0.0
    total_relevance = 0.0

    for dimension, requirement in (
        career_requirements.items()
    ):

        if requirement <= 0:
            continue

        total_relevance += requirement

        coverage_data = evidence_coverage.get(
            dimension,
            {},
        )

        coverage_value = coverage_data.get(
            "evidence_coverage",
            coverage_data.get(
                "coverage",
                0.0,
            ),
        )

        # Normalize 0-100 values to 0-1.

        if coverage_value > 1:
            coverage_value = (
                coverage_value / 100
            )

        weighted_coverage += (
            coverage_value
            * requirement
        )

    if total_relevance == 0:
        return 0.0

    return round(
        (
            weighted_coverage
            / total_relevance
        ) * 100,
        1,
    )


# ============================================================
# COMPONENT RESULT
# ============================================================

def calculate_component_result(
    student_scores,
    student_evidence,
    career_requirements,
):
    """
    Calculate one matching component.

    Components:

        Interest
        Aptitude
        Work Style
    """

    score = calculate_dimension_match(
        student_scores,
        career_requirements,
    )

    contributions = (
        calculate_dimension_contributions(
            student_scores,
            career_requirements,
        )
    )

    coverage = (
        calculate_component_evidence_coverage(
            student_scores,
            student_evidence,
            career_requirements,
        )
    )

    return {
        "score": score,
        "evidence_coverage": coverage,
        "contributions": contributions,
    }


# ============================================================
# OVERALL CAREER MATCH
# ============================================================

def calculate_career_match(
    interest_profile,
    aptitude_profile,
    work_style_profile,
    career_profile,
    education_level=None,
):
    """
    Calculate the complete match between one student
    and one career.

    Returns a structured result that can later be used
    by the UI and explanation engine.
    """

    # --------------------------------------------------------
    # Extract student data
    # --------------------------------------------------------

    interest_scores = interest_profile.get(
        "scores",
        {},
    )

    aptitude_scores = aptitude_profile.get(
        "scores",
        {},
    )

    work_style_scores = work_style_profile.get(
        "scores",
        {},
    )

    interest_evidence = interest_profile.get(
        "evidence_coverage",
        {},
    )

    aptitude_evidence = aptitude_profile.get(
        "evidence_coverage",
        {},
    )

    work_style_evidence = work_style_profile.get(
        "evidence_coverage",
        {},
    )

    # --------------------------------------------------------
    # Calculate individual components
    # --------------------------------------------------------

    interest_result = calculate_component_result(
        interest_scores,
        interest_evidence,
        career_profile[
            "interest_requirements"
        ],
    )

    aptitude_result = calculate_component_result(
        aptitude_scores,
        aptitude_evidence,
        career_profile[
            "aptitude_requirements"
        ],
    )

    work_style_result = calculate_component_result(
        work_style_scores,
        work_style_evidence,
        career_profile[
            "work_style_requirements"
        ],
    )

    # --------------------------------------------------------
    # Weighted overall score
    # --------------------------------------------------------

    overall_score = (
        interest_result["score"]
        * MATCHING_WEIGHTS["interest"]

        +

        aptitude_result["score"]
        * MATCHING_WEIGHTS["aptitude"]

        +

        work_style_result["score"]
        * MATCHING_WEIGHTS["work_style"]
    )

    overall_score = round(overall_score,2)
    overall_score = apply_education_boost(overall_score, career_profile.get("career_id"), education_level)

    # --------------------------------------------------------
    # Overall evidence coverage
    # --------------------------------------------------------

    overall_evidence = (
        interest_result[
            "evidence_coverage"
        ]
        * MATCHING_WEIGHTS["interest"]

        +

        aptitude_result[
            "evidence_coverage"
        ]
        * MATCHING_WEIGHTS["aptitude"]

        +

        work_style_result[
            "evidence_coverage"
        ]
        * MATCHING_WEIGHTS["work_style"]
    )

    overall_evidence = round(
        overall_evidence,
        1,
    )

    # --------------------------------------------------------
    # Recommendation level
    # --------------------------------------------------------

    recommendation = classify_match(
        overall_score
    )

    # --------------------------------------------------------
    # Strongest dimensions
    # --------------------------------------------------------

    strongest_dimensions = (
        get_strongest_dimensions(
            interest_result,
            aptitude_result,
            work_style_result,
        )
    )

    # --------------------------------------------------------
    # Development areas
    # --------------------------------------------------------

    development_areas = (
        get_development_areas(
            interest_result,
            aptitude_result,
            work_style_result,
        )
    )

    return {
        "career_id": career_profile.get(
            "career_id"
        ),

        "career_name": career_profile[
            "name"
        ],

        "domain": career_profile[
            "domain"
        ],

        "description": career_profile[
            "description"
        ],

        "overall_match": overall_score,

        "recommendation": recommendation,

        "evidence_coverage": overall_evidence,

        "components": {
            "interest": interest_result,

            "aptitude": aptitude_result,

            "work_style": work_style_result,
        },

        "strongest_dimensions": (
            strongest_dimensions
        ),

        "development_areas": (
            development_areas
        ),

        "core_skills": career_profile[
            "core_skills"
        ],

        "education_notes": career_profile[
            "education_notes"
        ],
    }


# ============================================================
# MATCH CLASSIFICATION
# ============================================================

def classify_match(score):
    """
    Convert the numerical score into a user-friendly
    recommendation level.

    These are recommendation categories,
    NOT acceptance/rejection decisions.
    """

    if score >= 80:
        return "Strong Match"

    if score >= 65:
        return "Good Match"

    if score >= 50:
        return "Moderate Match"

    if score >= 35:
        return "Explore Further"

    return "Low Alignment"


# ============================================================
# STRONGEST DIMENSIONS
# ============================================================

def get_strongest_dimensions(
    interest_result,
    aptitude_result,
    work_style_result,
    top_n=5,
):
    """
    Find dimensions where the student's score contributes
    strongly to the career match.
    """

    all_dimensions = []

    # --------------------------------------------------------
    # Interest
    # --------------------------------------------------------

    for item in interest_result[
        "contributions"
    ]:

        all_dimensions.append(
            {
                "dimension": item[
                    "dimension"
                ],
                "category": "Interest",
                "student_score": item[
                    "student_score"
                ],
                "career_requirement": item[
                    "career_requirement"
                ],
                "contribution": item[
                    "contribution"
                ],
            }
        )

    # --------------------------------------------------------
    # Aptitude
    # --------------------------------------------------------

    for item in aptitude_result[
        "contributions"
    ]:

        all_dimensions.append(
            {
                "dimension": item[
                    "dimension"
                ],
                "category": "Aptitude",
                "student_score": item[
                    "student_score"
                ],
                "career_requirement": item[
                    "career_requirement"
                ],
                "contribution": item[
                    "contribution"
                ],
            }
        )

    # --------------------------------------------------------
    # Work Style
    # --------------------------------------------------------

    for item in work_style_result[
        "contributions"
    ]:

        all_dimensions.append(
            {
                "dimension": item[
                    "dimension"
                ],
                "category": "Work Style",
                "student_score": item[
                    "student_score"
                ],
                "career_requirement": item[
                    "career_requirement"
                ],
                "contribution": item[
                    "contribution"
                ],
            }
        )

    # --------------------------------------------------------
    # Sort by contribution
    # --------------------------------------------------------

    all_dimensions.sort(
        key=lambda item: (
            item["contribution"]
        ),
        reverse=True,
    )

    return all_dimensions[:top_n]


# ============================================================
# DEVELOPMENT AREAS
# ============================================================

def get_development_areas(
    interest_result,
    aptitude_result,
    work_style_result,
    top_n=5,
):
    """
    Identify relevant dimensions where the student's
    current score is comparatively lower.

    This does NOT mean the student is incapable.

    It means:

        "This is an area worth developing if you
         pursue this career direction."
    """

    all_dimensions = []

    component_data = [
        (
            "Interest",
            interest_result,
        ),

        (
            "Aptitude",
            aptitude_result,
        ),

        (
            "Work Style",
            work_style_result,
        ),
    ]

    for category, result in component_data:

        for item in result[
            "contributions"
        ]:

            student_score = item[
                "student_score"
            ]

            career_requirement = item[
                "career_requirement"
            ]

            # Only consider dimensions that the
            # career genuinely values.

            if career_requirement < 5:
                continue

            gap = (
                career_requirement
                - student_score
            )

            if gap <= 0:
                continue

            all_dimensions.append(
                {
                    "dimension": item[
                        "dimension"
                    ],

                    "category": category,

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
                }
            )

    all_dimensions.sort(
        key=lambda item: item["gap"],
        reverse=True,
    )

    return all_dimensions[:top_n]


# ============================================================
# MATCH ONE CAREER BY ID
# ============================================================

def match_student_to_career(
    interest_profile,
    aptitude_profile,
    work_style_profile,
    career_id,
    education_level=None,
):
    """
    Match a student against one career ID.
    """

    if career_id not in CAREER_PROFILES:
        raise ValueError(
            f"Unknown career ID: {career_id}"
        )

    career_profile = CAREER_PROFILES[
        career_id
    ].copy()

    # Add career ID to the result.

    career_profile["career_id"] = (
        career_id
    )

    return calculate_career_match(
        interest_profile,
        aptitude_profile,
        work_style_profile,
        career_profile,
        education_level,
    )


# ============================================================
# MATCH AGAINST ALL CAREERS
# ============================================================

def match_student_to_all_careers(
    interest_profile,
    aptitude_profile,
    work_style_profile,
    education_level=None,
):
    """
    Calculate matches for every career in the knowledge base.

    Returns a list sorted by overall match score.
    """

    results = []

    for career_id in CAREER_PROFILES:

        result = match_student_to_career(
            interest_profile,
            aptitude_profile,
            work_style_profile,
            career_id,
            education_level,
        )

        results.append(result)

    # Highest score first.

    results.sort(
        key=lambda result: (
            result["overall_match"]
        ),
        reverse=True,
    )

    return results


# ============================================================
# TOP CAREER RECOMMENDATIONS
# ============================================================

def get_top_career_recommendations(
    interest_profile,
    aptitude_profile,
    work_style_profile,
    education_level=None,
    top_n=3,
):
    """
    Return the top N career directions.
    """

    all_results = match_student_to_all_careers(
        interest_profile,
        aptitude_profile,
        work_style_profile,
        education_level,
    )

    return all_results[:top_n]


# ============================================================
# PRINT CAREER RESULT
# ============================================================

def print_career_result(result):
    """
    Print a human-readable career recommendation.
    """

    print()
    print("-" * 75)

    print(
        f"{result['career_name']} "
        f"({result['domain']})"
    )

    print(
        f"Match: "
        f"{result['overall_match']:.2f}%"
    )

    print(
        f"Recommendation: "
        f"{result['recommendation']}"
    )

    print(
        f"Evidence coverage: "
        f"{result['evidence_coverage']:.1f}%"
    )

    print()

    print("Component scores:")

    print(
        f"  Interest:   "
        f"{result['components']['interest']['score']:.2f}%"
    )

    print(
        f"  Aptitude:   "
        f"{result['components']['aptitude']['score']:.2f}%"
    )

    print(
        f"  Work Style: "
        f"{result['components']['work_style']['score']:.2f}%"
    )

    print()

    print("Strongest matching areas:")

    for item in result[
        "strongest_dimensions"
    ]:

        print(
            f"  - "
            f"{item['category']}: "
            f"{item['dimension']} "
            f"(student "
            f"{item['student_score']:.2f}/10, "
            f"career relevance "
            f"{item['career_requirement']:.2f}/10)"
        )

    print()

    print("Development areas:")

    if not result[
        "development_areas"
    ]:

        print(
            "  - No major development gap identified."
        )

    else:

        for item in result[
            "development_areas"
        ]:

            print(
                f"  - "
                f"{item['category']}: "
                f"{item['dimension']} "
                f"(current "
                f"{item['student_score']:.2f}/10, "
                f"career relevance "
                f"{item['career_requirement']:.2f}/10)"
            )


# ============================================================
# TEST DATA
# ============================================================

def build_test_student_profiles():
    """
    Build Student A and Student B using the CURRENT
    profile modules.

    This function is used only for testing the
    Career Matching Engine.

    It does NOT affect the actual application.
    """

    # --------------------------------------------------------
    # INTEREST PROFILE
    # --------------------------------------------------------

    from student_profile import (
        build_interest_profile,

        STUDENT_A_PREFERENCE_ANSWERS
        as INTEREST_A_PREFERENCES,

        STUDENT_A_DIRECT_RATINGS
        as INTEREST_A_RATINGS,

        STUDENT_B_PREFERENCE_ANSWERS
        as INTEREST_B_PREFERENCES,

        STUDENT_B_DIRECT_RATINGS
        as INTEREST_B_RATINGS,
    )

    # --------------------------------------------------------
    # APTITUDE PROFILE
    # --------------------------------------------------------

    from aptitude_profile import (
        build_aptitude_profile,

        STUDENT_A_ANSWERS
        as APTITUDE_A,

        STUDENT_B_ANSWERS
        as APTITUDE_B,
    )

    # --------------------------------------------------------
    # WORK-STYLE PROFILE
    # --------------------------------------------------------

    from work_style_profile import (
        build_work_style_profile,

        STUDENT_A_PREFERENCE_ANSWERS
        as WORK_A_PREFERENCES,

        STUDENT_A_DIRECT_RATINGS
        as WORK_A_RATINGS,

        STUDENT_B_PREFERENCE_ANSWERS
        as WORK_B_PREFERENCES,

        STUDENT_B_DIRECT_RATINGS
        as WORK_B_RATINGS,
    )

    # ========================================================
    # STUDENT A — INTEREST
    # ========================================================

    student_a_interest = build_interest_profile(
        preference_answers=(
            INTEREST_A_PREFERENCES
        ),

        direct_ratings=(
            INTEREST_A_RATINGS
        ),
    )

    # ========================================================
    # STUDENT A — APTITUDE
    # ========================================================

    student_a_aptitude = build_aptitude_profile(
        APTITUDE_A
    )

    # ========================================================
    # STUDENT A — WORK STYLE
    # ========================================================

    student_a_work_style = build_work_style_profile(
        preference_answers=(
            WORK_A_PREFERENCES
        ),

        direct_ratings=(
            WORK_A_RATINGS
        ),
    )

    # ========================================================
    # STUDENT A — COMPLETE PROFILE
    # ========================================================

    student_a = {
        "interest": student_a_interest,

        "aptitude": student_a_aptitude,

        "work_style": student_a_work_style,
    }

    # ========================================================
    # STUDENT B — INTEREST
    # ========================================================

    student_b_interest = build_interest_profile(
        preference_answers=(
            INTEREST_B_PREFERENCES
        ),

        direct_ratings=(
            INTEREST_B_RATINGS
        ),
    )

    # ========================================================
    # STUDENT B — APTITUDE
    # ========================================================

    student_b_aptitude = build_aptitude_profile(
        APTITUDE_B
    )

    # ========================================================
    # STUDENT B — WORK STYLE
    # ========================================================

    student_b_work_style = build_work_style_profile(
        preference_answers=(
            WORK_B_PREFERENCES
        ),

        direct_ratings=(
            WORK_B_RATINGS
        ),
    )

    # ========================================================
    # STUDENT B — COMPLETE PROFILE
    # ========================================================

    student_b = {
        "interest": student_b_interest,

        "aptitude": student_b_aptitude,

        "work_style": student_b_work_style,
    }

    return student_a, student_b


# ============================================================
# MAIN TEST
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Validate career knowledge base
    # --------------------------------------------------------

    validate_career_profiles()

    # --------------------------------------------------------
    # Validate matching weights
    # --------------------------------------------------------

    validate_matching_weights()

    print(
        "Career matching engine validation successful."
    )

    print()

    print(
        "Matching weights:"
    )

    print(
        f"  Interest:   "
        f"{MATCHING_WEIGHTS['interest'] * 100:.0f}%"
    )

    print(
        f"  Aptitude:   "
        f"{MATCHING_WEIGHTS['aptitude'] * 100:.0f}%"
    )

    print(
        f"  Work Style: "
        f"{MATCHING_WEIGHTS['work_style'] * 100:.0f}%"
    )

    print()

    # --------------------------------------------------------
    # Build test students
    # --------------------------------------------------------

    student_a, student_b = (
        build_test_student_profiles()
    )

    # ========================================================
    # STUDENT A
    # ========================================================

    print("=" * 80)

    print(
        "STUDENT A — TOP CAREER DIRECTIONS"
    )

    print("=" * 80)

    student_a_results = (
        get_top_career_recommendations(
            student_a["interest"],

            student_a["aptitude"],

            student_a["work_style"],

            top_n=5,
        )
    )

    for index, result in enumerate(
        student_a_results,
        start=1,
    ):

        print(
            f"\n{index}. "
            f"{result['career_name']} "
            f"— "
            f"{result['overall_match']:.2f}% "
            f"— "
            f"{result['recommendation']}"
        )

    # --------------------------------------------------------
    # Detailed first recommendation
    # --------------------------------------------------------

    if student_a_results:

        print()

        print("=" * 80)

        print(
            "STUDENT A — DETAILED TOP MATCH"
        )

        print("=" * 80)

        print_career_result(
            student_a_results[0]
        )

    # ========================================================
    # STUDENT B
    # ========================================================

    print()

    print("=" * 80)

    print(
        "STUDENT B — TOP CAREER DIRECTIONS"
    )

    print("=" * 80)

    student_b_results = (
        get_top_career_recommendations(
            student_b["interest"],

            student_b["aptitude"],

            student_b["work_style"],

            top_n=5,
        )
    )

    for index, result in enumerate(
        student_b_results,
        start=1,
    ):

        print(
            f"\n{index}. "
            f"{result['career_name']} "
            f"— "
            f"{result['overall_match']:.2f}% "
            f"— "
            f"{result['recommendation']}"
        )

    # --------------------------------------------------------
    # Detailed first recommendation
    # --------------------------------------------------------

    if student_b_results:

        print()

        print("=" * 80)

        print(
            "STUDENT B — DETAILED TOP MATCH"
        )

        print("=" * 80)

        print_career_result(
            student_b_results[0]
        )

    # ========================================================
    # FINAL STATUS
    # ========================================================

    print()

    print("=" * 80)

    print(
        "Career matching test completed successfully."
    )

    print(
        "The scores are recommendation signals, "
        "not career decisions."
    )
