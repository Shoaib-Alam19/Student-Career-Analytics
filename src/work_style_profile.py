"""
Short Work Style Engine for Student Career Navigator.
"""

WORK_STYLE_DIMENSIONS = [
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
]


WORK_STYLE_QUESTIONS = [

    {
        "question_id": "workstyle_01",
        "question": (
            "You are given a project. "
            "Which setup sounds most natural?"
        ),
        "options": {

            "A": {
                "text": (
                    "Work with teammates and "
                    "divide responsibilities"
                ),
                "scores": {
                    "teamwork": 3,
                    "people_interaction": 1,
                },
            },

            "B": {
                "text": (
                    "Work independently and "
                    "own the solution"
                ),
                "scores": {
                    "independent_work": 3,
                    "research_work": 1,
                },
            },

            "C": {
                "text": (
                    "Lead the group and "
                    "coordinate the plan"
                ),
                "scores": {
                    "leadership": 3,
                    "structured_work": 1,
                },
            },

            "D": {
                "text": (
                    "Choose your own process "
                    "and experiment"
                ),
                "scores": {
                    "flexible_work": 3,
                    "creative_work": 1,
                },
            },
        },
    },

    {
        "question_id": "workstyle_02",
        "question": (
            "Which kind of task would "
            "you enjoy most?"
        ),
        "options": {

            "A": {
                "text": (
                    "Analyze data and "
                    "find useful patterns"
                ),
                "scores": {
                    "data_work": 3,
                    "research_work": 1,
                },
            },

            "B": {
                "text": (
                    "Build or improve "
                    "a technology solution"
                ),
                "scores": {
                    "technology_work": 3,
                    "creative_work": 1,
                },
            },

            "C": {
                "text": (
                    "Talk with people and "
                    "understand their needs"
                ),
                "scores": {
                    "people_interaction": 3,
                    "helping_others": 1,
                },
            },

            "D": {
                "text": (
                    "Solve a problem by "
                    "following a clear process"
                ),
                "scores": {
                    "structured_work": 3,
                    "independent_work": 1,
                },
            },
        },
    },

    {
        "question_id": "workstyle_03",
        "question": (
            "Where would you rather "
            "spend a workday?"
        ),
        "options": {

            "A": {
                "text": (
                    "Mostly at a desk "
                    "with digital tools"
                ),
                "scores": {
                    "technology_work": 2,
                    "data_work": 2,
                },
            },

            "B": {
                "text": (
                    "Moving between "
                    "real-world locations"
                ),
                "scores": {
                    "field_work": 3,
                    "people_interaction": 1,
                },
            },

            "C": {
                "text": (
                    "In a collaborative "
                    "team environment"
                ),
                "scores": {
                    "teamwork": 2,
                    "helping_others": 2,
                },
            },

            "D": {
                "text": (
                    "In a quiet space where "
                    "you can focus deeply"
                ),
                "scores": {
                    "independent_work": 2,
                    "research_work": 2,
                },
            },
        },
    },

    {
        "question_id": "workstyle_04",
        "question": (
            "When plans change suddenly, "
            "what feels best?"
        ),
        "options": {

            "A": {
                "text": (
                    "Adapt quickly and "
                    "find a new approach"
                ),
                "scores": {
                    "flexible_work": 3,
                    "creative_work": 1,
                },
            },

            "B": {
                "text": (
                    "Reorganize the plan "
                    "and restore structure"
                ),
                "scores": {
                    "structured_work": 3,
                    "leadership": 1,
                },
            },

            "C": {
                "text": (
                    "Discuss the change "
                    "with the people involved"
                ),
                "scores": {
                    "people_interaction": 2,
                    "teamwork": 2,
                },
            },

            "D": {
                "text": (
                    "Investigate the situation "
                    "before acting"
                ),
                "scores": {
                    "research_work": 2,
                    "data_work": 2,
                },
            },
        },
    },

    {
        "question_id": "workstyle_05",
        "question": (
            "What feels most rewarding "
            "at the end of a project?"
        ),
        "options": {

            "A": {
                "text": (
                    "Knowing your work "
                    "directly helped someone"
                ),
                "scores": {
                    "helping_others": 3,
                    "people_interaction": 1,
                },
            },

            "B": {
                "text": (
                    "Seeing a creative "
                    "idea become real"
                ),
                "scores": {
                    "creative_work": 3,
                    "flexible_work": 1,
                },
            },

            "C": {
                "text": (
                    "Seeing the team succeed "
                    "through good coordination"
                ),
                "scores": {
                    "leadership": 2,
                    "teamwork": 2,
                },
            },

            "D": {
                "text": (
                    "Having clear evidence "
                    "that the solution works"
                ),
                "scores": {
                    "data_work": 2,
                    "technology_work": 2,
                },
            },
        },
    },

    {
        "question_id": "workstyle_06",
        "question": (
            "Which work rhythm "
            "would you prefer?"
        ),
        "options": {

            "A": {
                "text": (
                    "A predictable routine "
                    "with clear expectations"
                ),
                "scores": {
                    "structured_work": 2,
                    "independent_work": 2,
                },
            },

            "B": {
                "text": (
                    "A changing day "
                    "with new situations"
                ),
                "scores": {
                    "flexible_work": 2,
                    "field_work": 2,
                },
            },

            "C": {
                "text": (
                    "A mix of research, analysis, "
                    "and problem-solving"
                ),
                "scores": {
                    "research_work": 2,
                    "data_work": 2,
                },
            },

            "D": {
                "text": (
                    "A mix of people, technology, "
                    "and collaboration"
                ),
                "scores": {
                    "people_interaction": 2,
                    "technology_work": 2,
                },
            },
        },
    },
]


DIRECT_WORK_STYLE_RATINGS = []


def create_work_style_evidence():

    return {
        dimension: {
            "preference_earned": 0.0,
            "preference_maximum": 0.0,
            "questions_answered": set(),
            "relevant_questions": 0,
            "direct_rating": None,
            "direct_rating_present": False,
        }
        for dimension in WORK_STYLE_DIMENSIONS
    }


def apply_work_style_answer(
    evidence,
    question_id,
    answer,
):

    question = next(
        (
            question
            for question in WORK_STYLE_QUESTIONS
            if question["question_id"] == question_id
        ),
        None,
    )

    if question is None:
        raise ValueError(
            f"Unknown work-style question: "
            f"{question_id}"
        )

    if answer not in question["options"]:
        raise ValueError(
            f"Invalid answer '{answer}' "
            f"for {question_id}"
        )

    for dimension in WORK_STYLE_DIMENSIONS:

        maximum_score = max(
            option["scores"].get(
                dimension,
                0,
            )
            for option in question[
                "options"
            ].values()
        )

        if maximum_score > 0:

            evidence[dimension][
                "preference_maximum"
            ] += maximum_score

            evidence[dimension][
                "relevant_questions"
            ] += 1

            evidence[dimension][
                "questions_answered"
            ].add(question_id)

    selected_scores = question[
        "options"
    ][answer]["scores"]

    for dimension, points in selected_scores.items():

        evidence[dimension][
            "preference_earned"
        ] += points


def calculate_work_style_scores(
    evidence,
):

    return {
        dimension: round(
            (
                item["preference_earned"]
                /
                item["preference_maximum"]
            )
            * 10,
            2,
        )
        if item["preference_maximum"]
        else 0.0

        for dimension, item
        in evidence.items()
    }


def calculate_work_style_evidence_coverage(
    evidence,
):

    coverage = {}

    for dimension, item in evidence.items():

        relevant = (
            item["relevant_questions"]
        )

        answered = len(
            item["questions_answered"]
        )

        percentage = (
            answered / relevant * 100
            if relevant
            else 0.0
        )

        coverage[dimension] = {

            "relevant_questions":
                relevant,

            "answered_questions":
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


def build_work_style_profile(
    preference_answers=None,
    direct_ratings=None,
):

    evidence = (
        create_work_style_evidence()
    )

    for question_id, answer in (
        (preference_answers or {}).items()
    ):

        apply_work_style_answer(
            evidence,
            question_id,
            answer,
        )

    return {

        "evidence":
            evidence,

        "scores":
            calculate_work_style_scores(
                evidence
            ),

        "evidence_coverage":
            calculate_work_style_evidence_coverage(
                evidence
            ),
    }


def validate_question_bank():

    if len(WORK_STYLE_QUESTIONS) != 6:

        raise ValueError(
            "Expected exactly 6 work-style questions."
        )

    covered = {
        dimension: 0
        for dimension in WORK_STYLE_DIMENSIONS
    }

    for question in WORK_STYLE_QUESTIONS:

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
            f"Work-style dimensions not covered: "
            f"{missing}"
        )

    return True


if __name__ == "__main__":

    validate_question_bank()

    print(
        "Short work-style question bank "
        "validation successful."
    )

    print(
        f"Questions: {len(WORK_STYLE_QUESTIONS)}"
    )