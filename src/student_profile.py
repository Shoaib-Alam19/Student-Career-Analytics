"""
Short Interest Profile Engine for Student Career Navigator.
"""

INTEREST_DIMENSIONS = [
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
]


INTEREST_QUESTIONS = [
    {
        "question_id": "interest_01",
        "question": "Which activity would you rather spend an afternoon doing?",
        "options": {
            "A": {
                "text": "Build an app or explore a new technology",
                "scores": {
                    "technology": 3,
                    "research": 1,
                },
            },
            "B": {
                "text": "Understand how the human body works",
                "scores": {
                    "biology_health": 3,
                    "science": 1,
                },
            },
            "C": {
                "text": "Create a visual design or piece of content",
                "scores": {
                    "creative_arts": 3,
                    "media": 1,
                },
            },
            "D": {
                "text": "Understand how a business grows and makes money",
                "scores": {
                    "business": 3,
                    "finance": 1,
                },
            },
        },
    },

    {
        "question_id": "interest_02",
        "question": "Which problem sounds most satisfying to solve?",
        "options": {
            "A": {
                "text": "Find patterns in numbers or data",
                "scores": {
                    "mathematics": 3,
                    "research": 1,
                },
            },
            "B": {
                "text": "Find a practical way to help someone",
                "scores": {
                    "people_helping": 3,
                    "communication": 1,
                },
            },
            "C": {
                "text": "Understand a law, right, or justice issue",
                "scores": {
                    "law": 3,
                    "social_issues": 1,
                },
            },
            "D": {
                "text": "Understand an environmental problem",
                "scores": {
                    "nature_environment": 3,
                    "science": 1,
                },
            },
        },
    },

    {
        "question_id": "interest_03",
        "question": "What would you naturally choose to learn more about?",
        "options": {
            "A": {
                "text": "Government, policy, or public administration",
                "scores": {
                    "public_service": 3,
                    "social_issues": 1,
                },
            },
            "B": {
                "text": "Writing, speaking, or explaining ideas",
                "scores": {
                    "communication": 3,
                    "media": 1,
                },
            },
            "C": {
                "text": "Money, investing, or financial decisions",
                "scores": {
                    "finance": 3,
                    "mathematics": 1,
                },
            },
            "D": {
                "text": "Science experiments and how things work",
                "scores": {
                    "science": 3,
                    "research": 1,
                },
            },
        },
    },

    {
        "question_id": "interest_04",
        "question": "Which project would excite you most?",
        "options": {
            "A": {
                "text": "Build a useful digital tool",
                "scores": {
                    "technology": 3,
                    "creative_arts": 1,
                },
            },
            "B": {
                "text": "Study a health or medical problem",
                "scores": {
                    "biology_health": 3,
                    "research": 1,
                },
            },
            "C": {
                "text": "Investigate an important social issue",
                "scores": {
                    "social_issues": 3,
                    "public_service": 1,
                },
            },
            "D": {
                "text": "Create a campaign for a product or idea",
                "scores": {
                    "media": 3,
                    "business": 1,
                },
            },
        },
    },

    {
        "question_id": "interest_05",
        "question": "Which challenge sounds most appealing?",
        "options": {
            "A": {
                "text": "Solve a complex numerical problem",
                "scores": {
                    "mathematics": 3,
                    "finance": 1,
                },
            },
            "B": {
                "text": "Defend an argument about an important issue",
                "scores": {
                    "law": 3,
                    "communication": 1,
                },
            },
            "C": {
                "text": "Design something people enjoy using",
                "scores": {
                    "creative_arts": 3,
                    "technology": 1,
                },
            },
            "D": {
                "text": "Coach, teach, or support someone",
                "scores": {
                    "people_helping": 3,
                    "biology_health": 1,
                },
            },
        },
    },

    {
        "question_id": "interest_06",
        "question": "Which weekend activity sounds best?",
        "options": {
            "A": {
                "text": "Learn a programming or technical concept",
                "scores": {
                    "technology": 3,
                    "mathematics": 1,
                },
            },
            "B": {
                "text": "Train, play sport, or work on fitness",
                "scores": {
                    "physical_activity": 3,
                    "biology_health": 1,
                },
            },
            "C": {
                "text": "Explore a natural place and its environment",
                "scores": {
                    "nature_environment": 3,
                    "science": 1,
                },
            },
            "D": {
                "text": "Make a video, podcast, or digital story",
                "scores": {
                    "media": 3,
                    "communication": 1,
                },
            },
        },
    },

    {
        "question_id": "interest_07",
        "question": "What kind of impact would feel most meaningful?",
        "options": {
            "A": {
                "text": "Make technology or systems work better",
                "scores": {
                    "technology": 2,
                    "research": 2,
                },
            },
            "B": {
                "text": "Improve people's health or wellbeing",
                "scores": {
                    "biology_health": 2,
                    "people_helping": 2,
                },
            },
            "C": {
                "text": "Improve society or public services",
                "scores": {
                    "social_issues": 2,
                    "public_service": 2,
                },
            },
            "D": {
                "text": "Build a successful organization or product",
                "scores": {
                    "business": 2,
                    "finance": 2,
                },
            },
        },
    },

    {
        "question_id": "interest_08",
        "question": "If you could spend a day exploring one area, which would you choose?",
        "options": {
            "A": {
                "text": "Data, statistics, or investigation",
                "scores": {
                    "mathematics": 2,
                    "research": 2,
                },
            },
            "B": {
                "text": "Law, rights, and justice",
                "scores": {
                    "law": 2,
                    "social_issues": 2,
                },
            },
            "C": {
                "text": "Design, art, and creative expression",
                "scores": {
                    "creative_arts": 2,
                    "media": 2,
                },
            },
            "D": {
                "text": "People, communication, and helping others",
                "scores": {
                    "communication": 2,
                    "people_helping": 2,
                },
            },
        },
    },
]


# Compatibility variable.
# The new UI does not use a separate rating questionnaire.
DIRECT_INTEREST_RATINGS = []


def create_interest_evidence():

    return {
        dimension: {
            "preference_earned": 0.0,
            "preference_maximum": 0.0,
            "preference_questions_answered": set(),
            "relevant_preference_questions": 0,
            "direct_rating": None,
            "direct_rating_present": False,
        }
        for dimension in INTEREST_DIMENSIONS
    }


def apply_interest_answer(
    evidence,
    question_id,
    answer,
):

    question = next(
        (
            question
            for question in INTEREST_QUESTIONS
            if question["question_id"] == question_id
        ),
        None,
    )

    if question is None:
        raise ValueError(
            f"Unknown question ID: {question_id}"
        )

    if answer not in question["options"]:
        raise ValueError(
            f"Invalid answer '{answer}' "
            f"for {question_id}"
        )

    for dimension in INTEREST_DIMENSIONS:

        maximum_score = max(
            option["scores"].get(
                dimension,
                0,
            )
            for option in question["options"].values()
        )

        if maximum_score > 0:

            evidence[dimension][
                "relevant_preference_questions"
            ] += 1

            evidence[dimension][
                "preference_maximum"
            ] += maximum_score

            evidence[dimension][
                "preference_questions_answered"
            ].add(question_id)

    selected_scores = question[
        "options"
    ][answer]["scores"]

    for dimension, points in selected_scores.items():

        evidence[dimension][
            "preference_earned"
        ] += points


def calculate_interest_scores(evidence):

    scores = {}

    for dimension in INTEREST_DIMENSIONS:

        item = evidence[dimension]

        if item["preference_maximum"] > 0:

            scores[dimension] = round(
                (
                    item["preference_earned"]
                    /
                    item["preference_maximum"]
                )
                * 10,
                2,
            )

        else:

            scores[dimension] = 0.0

    return scores


def calculate_interest_evidence_coverage(
    evidence,
):

    coverage = {}

    for dimension in INTEREST_DIMENSIONS:

        item = evidence[dimension]

        relevant = (
            item[
                "relevant_preference_questions"
            ]
        )

        answered = len(
            item[
                "preference_questions_answered"
            ]
        )

        percentage = (
            answered / relevant * 100
            if relevant
            else 0.0
        )

        coverage[dimension] = {

            "preference_questions_relevant":
                relevant,

            "preference_questions_answered":
                answered,

            "preference_coverage":
                round(
                    percentage,
                    1,
                ),

            "direct_rating_present":
                False,

            "evidence_coverage":
                round(
                    percentage,
                    1,
                ),
        }

    return coverage


def build_interest_profile(
    preference_answers=None,
    direct_ratings=None,
):

    preference_answers = (
        preference_answers or {}
    )

    evidence = (
        create_interest_evidence()
    )

    for question_id, answer in (
        preference_answers.items()
    ):

        apply_interest_answer(
            evidence,
            question_id,
            answer,
        )

    scores = calculate_interest_scores(
        evidence
    )

    coverage = (
        calculate_interest_evidence_coverage(
            evidence
        )
    )

    return {

        "evidence":
            evidence,

        "scores":
            scores,

        "evidence_coverage":
            coverage,
    }


def validate_question_bank():

    if len(INTEREST_QUESTIONS) != 8:

        raise ValueError(
            "Expected exactly 8 interest questions."
        )

    for question in INTEREST_QUESTIONS:

        if set(
            question["options"]
        ) != {"A", "B", "C", "D"}:

            raise ValueError(
                f"Invalid options in "
                f"{question['question_id']}."
            )

    covered = {
        dimension: 0
        for dimension in INTEREST_DIMENSIONS
    }

    for question in INTEREST_QUESTIONS:

        for option in question[
            "options"
        ].values():

            for dimension in option[
                "scores"
            ]:

                covered[dimension] += 1

    missing = [
        dimension
        for dimension, count
        in covered.items()
        if count == 0
    ]

    if missing:

        raise ValueError(
            f"Interest dimensions not covered: "
            f"{missing}"
        )

    return True


if __name__ == "__main__":

    validate_question_bank()

    print(
        "Short interest question bank "
        "validation successful."
    )

    print(
        f"Questions: {len(INTEREST_QUESTIONS)}"
    )