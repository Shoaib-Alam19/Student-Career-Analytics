"""
Short Aptitude Engine for Student Career Navigator.
"""

APTITUDE_DIMENSIONS = [
    "logical_reasoning",
    "numerical_ability",
    "analytical_thinking",
    "problem_solving",
    "verbal_ability",
    "spatial_reasoning",
    "creative_thinking",
    "attention_detail",
]


APTITUDE_QUESTIONS = [

    {
        "question_id": "aptitude_01",
        "question": "What comes next? 2, 4, 8, 16, ?",
        "options": {
            "A": "18",
            "B": "24",
            "C": "32",
            "D": "36",
        },
        "correct_answer": "C",
        "dimensions": {
            "logical_reasoning": 1.0,
            "numerical_ability": 1.0,
        },
    },

    {
        "question_id": "aptitude_02",
        "question": (
            "A product costs ₹800 after a 20% discount. "
            "What was its original price?"
        ),
        "options": {
            "A": "₹960",
            "B": "₹1,000",
            "C": "₹1,020",
            "D": "₹1,040",
        },
        "correct_answer": "B",
        "dimensions": {
            "numerical_ability": 1.0,
            "analytical_thinking": 1.0,
        },
    },

    {
        "question_id": "aptitude_03",
        "question": (
            "All programmers are problem-solvers. "
            "Ali is a programmer. What must be true?"
        ),
        "options": {
            "A": "Ali is a designer",
            "B": "Ali is a problem-solver",
            "C": "All problem-solvers are programmers",
            "D": "Ali is a manager",
        },
        "correct_answer": "B",
        "dimensions": {
            "logical_reasoning": 1.0,
            "verbal_ability": 1.0,
        },
    },

    {
        "question_id": "aptitude_04",
        "question": (
            "A class has 30 students. 18 like Python, "
            "15 like Java, and 8 like both. "
            "How many like at least one?"
        ),
        "options": {
            "A": "25",
            "B": "33",
            "C": "41",
            "D": "45",
        },
        "correct_answer": "B",
        "dimensions": {
            "analytical_thinking": 1.0,
            "problem_solving": 1.0,
        },
    },

    {
        "question_id": "aptitude_05",
        "question": (
            "Which word is closest in meaning to 'precise'?"
        ),
        "options": {
            "A": "Exact",
            "B": "Fast",
            "C": "Large",
            "D": "Flexible",
        },
        "correct_answer": "A",
        "dimensions": {
            "verbal_ability": 1.0,
            "attention_detail": 1.0,
        },
    },

    {
        "question_id": "aptitude_06",
        "question": (
            "A cube is painted on all six faces and cut into "
            "27 equal small cubes. How many small cubes have "
            "paint on exactly two faces?"
        ),
        "options": {
            "A": "8",
            "B": "12",
            "C": "16",
            "D": "24",
        },
        "correct_answer": "B",
        "dimensions": {
            "spatial_reasoning": 1.0,
            "logical_reasoning": 1.0,
        },
    },

    {
        "question_id": "aptitude_07",
        "question": (
            "You need to design a poster for two different "
            "audiences. What is the best first step?"
        ),
        "options": {
            "A": "Use the same design",
            "B": "Understand each audience before designing",
            "C": "Add as many colors as possible",
            "D": "Copy a popular poster",
        },
        "correct_answer": "B",
        "dimensions": {
            "creative_thinking": 1.0,
            "problem_solving": 1.0,
        },
    },

    {
        "question_id": "aptitude_08",
        "question": (
            "Which number is different? 12, 18, 24, 31, 36"
        ),
        "options": {
            "A": "12",
            "B": "18",
            "C": "31",
            "D": "36",
        },
        "correct_answer": "C",
        "dimensions": {
            "attention_detail": 1.0,
            "analytical_thinking": 1.0,
        },
    },

    {
        "question_id": "aptitude_09",
        "question": (
            "If CAT becomes DBU by moving each letter one step "
            "forward, DOG becomes:"
        ),
        "options": {
            "A": "EPH",
            "B": "EOH",
            "C": "FPH",
            "D": "DPG",
        },
        "correct_answer": "A",
        "dimensions": {
            "logical_reasoning": 1.0,
            "verbal_ability": 1.0,
        },
    },

    {
        "question_id": "aptitude_10",
        "question": (
            "You have urgent, important, and optional tasks. "
            "Which should normally be handled first?"
        ),
        "options": {
            "A": "Optional",
            "B": "Important but not urgent",
            "C": "Urgent",
            "D": "Whichever is easiest",
        },
        "correct_answer": "C",
        "dimensions": {
            "problem_solving": 1.0,
            "analytical_thinking": 1.0,
        },
    },

    {
        "question_id": "aptitude_11",
        "question": (
            "Which shape has the same number of lines of "
            "symmetry as a square?"
        ),
        "options": {
            "A": "Equilateral triangle",
            "B": "Rectangle",
            "C": "Circle",
            "D": "Scalene triangle",
        },
        "correct_answer": "A",
        "dimensions": {
            "spatial_reasoning": 1.0,
            "attention_detail": 1.0,
        },
    },

    {
        "question_id": "aptitude_12",
        "question": (
            "A problem has no obvious solution. "
            "Which approach is strongest?"
        ),
        "options": {
            "A": "Give up",
            "B": "Try one random answer",
            "C": "Break it into smaller parts and test ideas",
            "D": "Wait for someone else",
        },
        "correct_answer": "C",
        "dimensions": {
            "creative_thinking": 1.0,
            "problem_solving": 1.0,
        },
    },
]


def create_aptitude_evidence():

    return {
        dimension: {
            "earned": 0.0,
            "maximum": 0.0,
            "questions_answered": 0,
            "relevant_questions": 0,
        }
        for dimension in APTITUDE_DIMENSIONS
    }


def apply_aptitude_answer(
    evidence,
    question_id,
    answer,
):

    question = next(
        (
            question
            for question in APTITUDE_QUESTIONS
            if question["question_id"] == question_id
        ),
        None,
    )

    if question is None:
        raise ValueError(
            f"Unknown aptitude question: {question_id}"
        )

    if answer not in question["options"]:
        raise ValueError(
            f"Invalid answer '{answer}' "
            f"for {question_id}"
        )

    for dimension, weight in question[
        "dimensions"
    ].items():

        evidence[dimension][
            "maximum"
        ] += weight

        evidence[dimension][
            "relevant_questions"
        ] += 1

        evidence[dimension][
            "questions_answered"
        ] += 1

        if answer == question[
            "correct_answer"
        ]:

            evidence[dimension][
                "earned"
            ] += weight


def calculate_aptitude_scores(
    evidence,
):

    return {
        dimension: round(
            (
                item["earned"]
                /
                item["maximum"]
            )
            * 10,
            2,
        )
        if item["maximum"]
        else 0.0

        for dimension, item
        in evidence.items()
    }


def calculate_aptitude_evidence_coverage(
    evidence,
):

    return {

        dimension: {

            "relevant_questions":
                item["relevant_questions"],

            "answered_questions":
                item["questions_answered"],

            "coverage":
                round(
                    (
                        item["questions_answered"]
                        /
                        item["relevant_questions"]
                        * 100
                    )
                    if item["relevant_questions"]
                    else 0.0,
                    1,
                ),
        }

        for dimension, item
        in evidence.items()
    }


def build_aptitude_profile(
    answers=None,
):

    evidence = (
        create_aptitude_evidence()
    )

    for question_id, answer in (
        (answers or {}).items()
    ):

        apply_aptitude_answer(
            evidence,
            question_id,
            answer,
        )

    return {

        "evidence":
            evidence,

        "scores":
            calculate_aptitude_scores(
                evidence
            ),

        "evidence_coverage":
            calculate_aptitude_evidence_coverage(
                evidence
            ),
    }


def validate_question_bank():

    if len(APTITUDE_QUESTIONS) != 12:

        raise ValueError(
            "Expected exactly 12 aptitude questions."
        )

    for question in APTITUDE_QUESTIONS:

        if set(
            question["options"]
        ) != {"A", "B", "C", "D"}:

            raise ValueError(
                f"Invalid options in "
                f"{question['question_id']}."
            )

        if question[
            "correct_answer"
        ] not in question["options"]:

            raise ValueError(
                f"Invalid correct answer in "
                f"{question['question_id']}."
            )

    covered = {
        dimension: 0
        for dimension in APTITUDE_DIMENSIONS
    }

    for question in APTITUDE_QUESTIONS:

        for dimension in question[
            "dimensions"
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
            f"Aptitude dimensions not covered: "
            f"{missing}"
        )

    return True


if __name__ == "__main__":

    validate_question_bank()

    print(
        "Short aptitude question bank "
        "validation successful."
    )

    print(
        f"Questions: {len(APTITUDE_QUESTIONS)}"
    )