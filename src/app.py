"""
Student Career Navigator
------------------------

Main Streamlit application.

Pipeline:

    Student Profile
          ↓
    Interest Assessment
          ↓
    Aptitude Assessment
          ↓
    Work Style Assessment
          ↓
    Career Matching
          ↓
    Career Explanation
          ↓
    Skill Gap
          ↓
    Personalized Roadmap
"""

# ============================================================
# IMPORTS
# ============================================================

import streamlit as st
from textwrap import dedent

from student_profile import (
    INTEREST_QUESTIONS,
    build_interest_profile,
)

from aptitude_profile import (
    APTITUDE_QUESTIONS,
    build_aptitude_profile,
)

from work_style_profile import (
    WORK_STYLE_QUESTIONS,
    build_work_style_profile,
)

from career_matching import (
    get_top_career_recommendations,
)

from career_explanation import (
    generate_career_explanation,
)

from student_skills import (
    create_student_skill_profile,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Career Navigator",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# HTML HELPER
# ============================================================

def render_html(html):
    """
    Render custom HTML safely using Streamlit's native
    HTML renderer (avoids markdown/code-block interpretation
    issues that st.markdown() can introduce with indented HTML).
    """

    st.html(dedent(html))


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Inter:wght@400;500;600;700;800&display=swap');

/* ============================================================
   DESIGN TOKENS
   ============================================================ */

:root {
    --ink: #1C2621;
    --ink-2: #2A3B32;
    --paper: #FAF8F3;
    --card: #FFFFFF;
    --line: #E5E0D3;
    --gold: #BF8B2E;
    --gold-soft: rgba(191, 139, 46, 0.12);
    --gold-line: rgba(191, 139, 46, 0.35);
    --trail: #4F7A5D;
    --trail-soft: rgba(79, 122, 93, 0.12);
    --ember: #A8502E;
    --ember-soft: rgba(168, 80, 46, 0.08);
    --text: #232922;
    --muted: #6E7A6C;
    --muted-2: #97A197;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, sans-serif;
}

h1, h2, h3, h4,
.hero-title,
.section-title,
.career-name {
    font-family: 'Fraunces', Georgia, serif;
}

.stApp {
    background: var(--paper);
}

.main .block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* ============================================================
   SIDEBAR — "EXPEDITION LOG"
   ============================================================ */

[data-testid="stSidebar"] {
    background: var(--ink);
    border-right: 1px solid var(--ink-2);
}

[data-testid="stSidebar"] * {
    color: #F3F1E9;
}

.sidebar-brand {
    font-family: 'Fraunces', serif;
    font-size: 1.4rem;
    font-weight: 600;
    letter-spacing: 0.01em;
    margin-bottom: 0.2rem;
}

.sidebar-subtitle {
    color: #9CA89E !important;
    font-size: 0.83rem;
    line-height: 1.55;
    margin-bottom: 1.6rem;
    border-left: 2px solid var(--gold-line);
    padding-left: 0.7rem;
}

.sidebar-eyebrow {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #7C8A7E !important;
    margin: 0 0 0.6rem 0;
}

.sidebar-step {
    padding: 0.6rem 0.75rem;
    border-radius: 8px;
    margin-bottom: 0.4rem;
    font-size: 0.88rem;
    border-left: 2px solid transparent;
    transition: all 0.15s ease;
}

.sidebar-step-complete {
    background: rgba(79, 122, 93, 0.18);
    border-left: 2px solid var(--trail);
}

.sidebar-step-current {
    background: var(--gold-soft);
    border-left: 2px solid var(--gold);
    font-weight: 600;
}

.sidebar-step-pending {
    background: rgba(255, 255, 255, 0.03);
    color: #7C8A7E !important;
}

/* ============================================================
   HERO — "TRAILHEAD"
   ============================================================ */

.hero {
    position: relative;
    overflow: hidden;
    background:
        linear-gradient(135deg, var(--ink) 0%, var(--ink-2) 100%);
    padding: 3.2rem 3.2rem 3rem 3.2rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    color: white;
    box-shadow: 0 16px 40px rgba(28, 38, 33, 0.22);
}

/* subtle topographic contour texture */
.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    opacity: 0.16;
    background-image:
        repeating-radial-gradient(
            circle at 85% 20%,
            transparent 0,
            transparent 22px,
            rgba(255,255,255,0.5) 23px,
            transparent 24px,
            transparent 58px
        );
    pointer-events: none;
}

.hero-badge {
    position: relative;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(191, 139, 46, 0.18);
    border: 1px solid var(--gold-line);
    color: #E8CE96;
    padding: 0.38rem 0.85rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1.1rem;
}

.hero-title {
    position: relative;
    font-size: 2.75rem;
    font-weight: 600;
    line-height: 1.18;
    margin-bottom: 0.9rem;
    letter-spacing: -0.01em;
}

.hero-title i {
    font-style: italic;
    color: #E8CE96;
}

.hero-text {
    position: relative;
    font-size: 1.05rem;
    color: #D6DCD4;
    max-width: 700px;
    line-height: 1.65;
}

/* ============================================================
   SECTION HEADERS
   ============================================================ */

.section-label {
    color: var(--gold);
    font-size: 0.74rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.35rem;
}

.section-title {
    font-size: 1.75rem;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 0.45rem;
    letter-spacing: -0.01em;
}

.section-description {
    color: var(--muted);
    margin-bottom: 1.4rem;
    max-width: 640px;
    line-height: 1.6;
}

/* ============================================================
   CARDS
   ============================================================ */

.card {
    background: var(--card);
    border: 1px solid var(--line);
    border-left: 3px solid var(--gold);
    border-radius: 14px;
    padding: 1.35rem 1.5rem;
    box-shadow: 0 4px 16px rgba(28, 38, 33, 0.05);
    margin-bottom: 1rem;
}

.card h3 {
    margin-top: 0;
    font-size: 1.15rem;
}

.soft-card {
    background: #F5F2E9;
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 0.85rem 1rem;
    font-size: 0.92rem;
    color: var(--text);
}

/* ============================================================
   CAREER CARDS
   ============================================================ */

.career-card {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 1.4rem;
    min-height: 220px;
    box-shadow: 0 4px 16px rgba(28, 38, 33, 0.05);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    border-top: 3px solid var(--gold);
}

.career-rank {
    color: var(--gold);
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.career-name {
    font-size: 1.3rem;
    font-weight: 600;
    color: var(--text);
    margin-top: 0.35rem;
    line-height: 1.25;
}

.career-domain {
    color: var(--muted);
    font-size: 0.85rem;
    margin-top: 0.25rem;
}

.match-score {
    font-family: 'Fraunces', serif;
    font-size: 2.1rem;
    font-weight: 600;
    color: var(--trail);
    margin-top: 1rem;
}

.match-label {
    font-size: 0.82rem;
    color: var(--muted);
}

/* ============================================================
   RESULT BANNER
   ============================================================ */

.result-banner {
    background: linear-gradient(135deg, #F5F2E9, #FBF8F0);
    border: 1px solid var(--line);
    border-left: 3px solid var(--gold);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.5rem;
}

.result-banner h2 {
    margin: 0.3rem 0 0.2rem 0;
    color: var(--text);
}

.result-banner p {
    color: var(--muted);
    margin: 0;
}

/* ============================================================
   ROADMAP — "TRAIL STAGES"
   ============================================================ */

.roadmap-start {
    background: var(--gold-soft);
    border: 1px solid var(--gold-line);
    border-radius: 14px;
    padding: 1.35rem 1.5rem;
    margin-bottom: 1rem;
}

.roadmap-next {
    background: var(--trail-soft);
    border: 1px solid rgba(79, 122, 93, 0.35);
    border-radius: 14px;
    padding: 1.35rem 1.5rem;
    margin-bottom: 1rem;
}

.roadmap-later {
    background: #F5F2E9;
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 1.1rem 1.5rem;
    margin-bottom: 1rem;
}

.roadmap-start h3,
.roadmap-next h3 {
    margin: 0.25rem 0 0.35rem 0;
    font-size: 1.15rem;
}

.roadmap-start p,
.roadmap-next p {
    margin: 0;
    color: var(--text);
}

.roadmap-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
}

/* ============================================================
   DISCLAIMER
   ============================================================ */

.disclaimer {
    background: var(--ember-soft);
    border: 1px solid rgba(168, 80, 46, 0.28);
    border-radius: 12px;
    padding: 1rem 1.15rem;
    color: #7A3D22;
    font-size: 0.88rem;
    line-height: 1.55;
}

/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    color: var(--muted-2);
    font-size: 0.8rem;
    padding-top: 2rem;
    border-top: 1px solid var(--line);
    margin-top: 1.5rem;
}

/* ============================================================
   STREAMLIT NATIVE ELEMENT OVERRIDES
   ============================================================ */

.stButton > button {
    border-radius: 8px;
    font-weight: 600;
    min-height: 2.7rem;
    border: 1px solid var(--line);
}

.stButton > button[kind="primary"] {
    background: var(--ink);
    border: 1px solid var(--ink);
}

.stButton > button[kind="primary"]:hover {
    background: var(--ink-2);
    border: 1px solid var(--ink-2);
}

[data-testid="stMetricValue"] {
    font-family: 'Fraunces', serif;
    color: var(--text);
}

[data-testid="stMetricLabel"] {
    color: var(--muted);
}

.stProgress > div > div > div > div {
    background: var(--gold);
}

hr {
    border-color: var(--line);
}

/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    .hero {
        padding: 2rem 1.35rem;
        border-radius: 16px;
    }

    .hero-title {
        font-size: 2rem;
    }

    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

DEFAULT_STATE = {
    "student_profile": None,
    "interest_profile": None,
    "aptitude_profile": None,
    "work_style_profile": None,
    "student_skill_profile": None,
    "career_results": None,
    "career_explanations": None,
}

for key, default_value in DEFAULT_STATE.items():

    if key not in st.session_state:
        st.session_state[key] = default_value


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def readable_name(value):
    return (
        value
        .replace("_", " ")
        .strip()
        .title()
    )


def reset_dependent_results():

    st.session_state.interest_profile = None
    st.session_state.aptitude_profile = None
    st.session_state.work_style_profile = None
    st.session_state.student_skill_profile = None
    st.session_state.career_results = None
    st.session_state.career_explanations = None


def create_empty_skill_profile():

    student_mode = (
        st.session_state.student_profile[
            "student_mode"
        ]
    )

    return create_student_skill_profile(
        student_mode,
        {},
    )


def generate_career_results():

    skill_profile = create_empty_skill_profile()

    results = get_top_career_recommendations(
        st.session_state.interest_profile,
        st.session_state.aptitude_profile,
        st.session_state.work_style_profile,
        education_level=st.session_state.student_profile["education_level"],
        top_n=5,
    )

    explanations = []

    for result in results:

        explanation = generate_career_explanation(
            result,
            student_skill_profile=skill_profile,
        )

        explanations.append(explanation)

    st.session_state.student_skill_profile = skill_profile
    st.session_state.career_results = results
    st.session_state.career_explanations = explanations


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    render_html(
        """
        <div class="sidebar-brand">
            🧭 Career Navigator
        </div>

        <div class="sidebar-subtitle">
            Your personalized career exploration journey.
        </div>
        """
    )

    render_html(
        """
        <div class="sidebar-eyebrow">
            Expedition Log
        </div>
        """
    )

    sidebar_steps = [
        (
            "👤",
            "Student Profile",
            st.session_state.student_profile is not None,
        ),
        (
            "🧠",
            "Interests",
            st.session_state.interest_profile is not None,
        ),
        (
            "🧩",
            "Aptitude",
            st.session_state.aptitude_profile is not None,
        ),
        (
            "💼",
            "Work Style",
            st.session_state.work_style_profile is not None,
        ),
        (
            "🎯",
            "Career Results",
            st.session_state.career_results is not None,
        ),
    ]

    for icon, label, completed in sidebar_steps:

        if completed:

            css_class = (
                "sidebar-step "
                "sidebar-step-complete"
            )

            text = (
                f"✓ &nbsp; {icon} {label}"
            )

        else:

            css_class = (
                "sidebar-step "
                "sidebar-step-pending"
            )

            text = (
                f"○ &nbsp; {icon} {label}"
            )

        render_html(
            f"""
            <div class="{css_class}">
                {text}
            </div>
            """
        )

    st.divider()

    st.markdown(
        """
        **How it works**

        Your results combine:

        • Interests  
        • Aptitude  
        • Work style  
        • Current skill information

        The system provides career guidance signals,
        not a final career decision.
        """
    )


# ============================================================
# HERO
# ============================================================

render_html(
    """
    <div class="hero">

        <div class="hero-badge">
            🧭 A compass for your next step
        </div>

        <div class="hero-title">
            Find a career direction<br>
            that fits <i>you</i>.
        </div>

        <div class="hero-text">
            Understand your interests, discover your strengths,
            explore suitable career directions, identify skill
            gaps, and get a personalized learning roadmap.
        </div>

    </div>
    """
)


# ============================================================
# PROGRESS
# ============================================================

completed_stages = sum(
    [
        st.session_state.student_profile is not None,
        st.session_state.interest_profile is not None,
        st.session_state.aptitude_profile is not None,
        st.session_state.work_style_profile is not None,
    ]
)

render_html(
    """
    <div class="section-label">
        YOUR JOURNEY
    </div>

    <div class="section-title">
        Assessment Progress
    </div>
    """
)

st.progress(
    completed_stages / 4
)

st.caption(
    f"{completed_stages} of 4 assessment stages completed"
)


# ============================================================
# STEP 1 — STUDENT PROFILE
# ============================================================

st.divider()

render_html(
    """
    <div class="section-label">
        WAYPOINT 01
    </div>

    <div class="section-title">
        👤 Tell us about yourself
    </div>

    <div class="section-description">
        Start with a few basic details. You can continue
        to the career assessments after saving your profile.
    </div>
    """
)

with st.container(border=True):

    with st.form(
        "student_profile_form"
    ):

        col1, col2 = st.columns(
            [2, 1]
        )

        with col1:

            name = st.text_input(
                "Your Name",
                placeholder="e.g. Shoaib Alam",
            )

        with col2:

            age = st.number_input(
                "Age",
                min_value=10,
                max_value=60,
                value=18,
                step=1,
            )

        education_level = st.selectbox(
            "Current Education Level",
            [
                "School",
                "College",
                "University",
            ],
        )

        submitted = st.form_submit_button(
            "Continue to Assessment →",
            type="primary",
            use_container_width=True,
        )


if submitted:

    cleaned_name = name.strip()

    if not cleaned_name:

        st.error(
            "Please enter your name before continuing."
        )

    else:

        education_mapping = {
            "School": "school",
            "College": "college",
            "University": "college",
        }

        reset_dependent_results()

        st.session_state.student_profile = {

            "name": cleaned_name,

            "age": int(age),

            "education_level": education_level,

            "student_mode": education_mapping[
                education_level
            ],
        }

        st.success(
            "Profile saved successfully! 🎉"
        )


# ============================================================
# PROFILE SUMMARY
# ============================================================

if st.session_state.student_profile:

    profile = (
        st.session_state.student_profile
    )

    render_html(
        """
        <div class="card">

            <h3>
                ✨ Profile ready
            </h3>

        </div>
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Name",
            profile["name"],
        )

    with col2:

        st.metric(
            "Age",
            profile["age"],
        )

    with col3:

        st.metric(
            "Education",
            profile["education_level"],
        )


# ============================================================
# STEP 2 — INTEREST ASSESSMENT
# ============================================================

# STEP 2 — INTEREST ASSESSMENT

if st.session_state.student_profile:

    st.divider()

    render_html(
        """
        <div class="section-label">WAYPOINT 02</div>

        <div class="section-title">
            🧠 What pulls your curiosity?
        </div>

        <div class="section-description">
            8 quick choices. Pick what genuinely sounds
            interesting. There are no right or wrong answers.
        </div>
        """
    )

    st.caption(
        f"Quick discovery · "
        f"{len(INTEREST_QUESTIONS)} questions"
    )

    preference_answers = {}

    with st.container(border=True):

        for index, question_data in enumerate(
            INTEREST_QUESTIONS,
            start=1,
        ):

            labels = [
                f"{key}. {option['text']}"
                for key, option
                in question_data["options"].items()
            ]

            selected = st.radio(
                (
                    f"{index}/"
                    f"{len(INTEREST_QUESTIONS)} · "
                    f"{question_data['question']}"
                ),
                labels,
                key=(
                    "interest_pref_"
                    f"{question_data['question_id']}"
                ),
            )

            preference_answers[
                question_data["question_id"]
            ] = selected[0]

    if st.button(
        "Continue → Build My Interest Profile",
        type="primary",
        use_container_width=True,
    ):

        try:

            st.session_state.interest_profile = (
                build_interest_profile(
                    preference_answers=preference_answers
                )
            )

            st.session_state.aptitude_profile = None
            st.session_state.work_style_profile = None
            st.session_state.career_results = None
            st.session_state.career_explanations = None

            st.success(
                "Interest profile ready! 🎉"
            )

        except Exception as error:

            st.error(
                "Interest profile generation failed."
            )

            st.exception(error)


# ============================================================
# INTEREST RESULT
# ============================================================

if st.session_state.interest_profile:

    profile = (
        st.session_state.interest_profile
    )

    render_html(
        """
        <div class="card">
            <h3>
                📊 Your strongest interests
            </h3>
        </div>
        """
    )

    scores = profile["scores"]

    top_scores = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )[:5]

    cols = st.columns(
        len(top_scores)
    )

    for col, (
        dimension,
        score,
    ) in zip(
        cols,
        top_scores,
    ):

        with col:

            st.metric(
                readable_name(dimension),
                f"{score:.2f}/10",
            )

            st.progress(
                min(
                    max(
                        score / 10,
                        0.0,
                    ),
                    1.0,
                )
            )


# ============================================================
# STEP 3 — APTITUDE ASSESSMENT
# ============================================================

# STEP 3 — APTITUDE ASSESSMENT

if (
    st.session_state.student_profile
    and st.session_state.interest_profile
):

    st.divider()

    render_html(
        """
        <div class="section-label">WAYPOINT 03</div>

        <div class="section-title">
            🧩 How do you think?
        </div>

        <div class="section-description">
            12 quick challenges covering reasoning,
            numbers, problem-solving, language, detail,
            space, and creativity.
        </div>
        """
    )

    render_html(
        """
        <div class="disclaimer">
            <b>Quick note:</b>
            This is an educational career-guidance exercise,
            not an IQ test or clinically validated
            psychometric test.
        </div>
        """
    )

    aptitude_answers = {}

    with st.container(border=True):

        for index, question_data in enumerate(
            APTITUDE_QUESTIONS,
            start=1,
        ):

            labels = [
                f"{key}. {text}"
                for key, text
                in question_data["options"].items()
            ]

            selected = st.radio(
                (
                    f"{index}/"
                    f"{len(APTITUDE_QUESTIONS)} · "
                    f"{question_data['question']}"
                ),
                labels,
                key=(
                    "aptitude_"
                    f"{question_data['question_id']}"
                ),
            )

            aptitude_answers[
                question_data["question_id"]
            ] = selected[0]

    if st.button(
        "Continue → See My Thinking Profile",
        type="primary",
        use_container_width=True,
    ):

        try:

            st.session_state.aptitude_profile = (
                build_aptitude_profile(
                    aptitude_answers
                )
            )

            st.session_state.work_style_profile = None
            st.session_state.career_results = None
            st.session_state.career_explanations = None

            st.success(
                "Aptitude profile ready! 🎉"
            )

        except Exception as error:

            st.error(
                "Aptitude profile generation failed."
            )

            st.exception(error)


# ============================================================
# APTITUDE RESULT
# ============================================================

if st.session_state.aptitude_profile:

    profile = (
        st.session_state.aptitude_profile
    )

    render_html(
        """
        <div class="card">
            <h3>
                📈 Your aptitude profile
            </h3>
        </div>
        """
    )

    scores = profile["scores"]

    for dimension, score in sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    ):

        col1, col2 = st.columns(
            [2, 5]
        )

        with col1:

            st.write(
                f"**{readable_name(dimension)}**"
            )

        with col2:

            st.progress(
                min(
                    max(
                        score / 10,
                        0.0,
                    ),
                    1.0,
                )
            )

            st.caption(
                f"{score:.2f}/10"
            )


# ============================================================
# STEP 4 — WORK STYLE
# ============================================================

# STEP 4 — WORK STYLE

if (
    st.session_state.student_profile
    and st.session_state.interest_profile
    and st.session_state.aptitude_profile
):

    st.divider()

    render_html(
        """
        <div class="section-label">WAYPOINT 04</div>

        <div class="section-title">
            💼 What kind of work feels natural?
        </div>

        <div class="section-description">
            6 quick scenarios. Choose the option
            that feels most like you.
        </div>
        """
    )

    st.caption(
        f"Quick discovery · "
        f"{len(WORK_STYLE_QUESTIONS)} questions"
    )

    work_style_answers = {}

    with st.container(border=True):

        for index, question_data in enumerate(
            WORK_STYLE_QUESTIONS,
            start=1,
        ):

            labels = [
                f"{key}. {option['text']}"
                for key, option
                in question_data["options"].items()
            ]

            selected = st.radio(
                (
                    f"{index}/"
                    f"{len(WORK_STYLE_QUESTIONS)} · "
                    f"{question_data['question']}"
                ),
                labels,
                key=(
                    "work_style_"
                    f"{question_data['question_id']}"
                ),
            )

            work_style_answers[
                question_data["question_id"]
            ] = selected[0]

    if st.button(
        "🎯 Finish Assessment → "
        "Show My Career Directions",
        type="primary",
        use_container_width=True,
    ):

        try:

            st.session_state.work_style_profile = (
                build_work_style_profile(
                    preference_answers=work_style_answers
                )
            )

            st.session_state.career_results = None
            st.session_state.career_explanations = None

            st.success(
                "Work-style profile ready! 🎉"
            )

        except Exception as error:

            st.error(
                "Work-style profile generation failed."
            )

            st.exception(error)


# ============================================================
# WORK STYLE RESULT
# ============================================================

if st.session_state.work_style_profile:

    profile = (
        st.session_state.work_style_profile
    )

    render_html(
        """
        <div class="card">
            <h3>
                💼 Your work style preferences
            </h3>
        </div>
        """
    )

    scores = profile["scores"]

    top_scores = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )[:6]

    cols = st.columns(3)

    for index, (
        dimension,
        score,
    ) in enumerate(top_scores):

        with cols[index % 3]:

            st.metric(
                readable_name(dimension),
                f"{score:.2f}/10",
            )


# ============================================================
# CAREER MATCHING
# ============================================================

if (
    st.session_state.student_profile
    and st.session_state.interest_profile
    and st.session_state.aptitude_profile
    and st.session_state.work_style_profile
):

    st.divider()

    render_html(
        """
        <div class="section-label">
            YOUR RESULTS
        </div>

        <div class="section-title">
            🎯 Discover your career directions
        </div>

        <div class="section-description">
            Your interests, aptitude, and work style are now
            combined to identify career directions worth exploring.
        </div>
        """
    )

    with st.container(border=True):

        st.markdown(
            "### How your match is calculated"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Interest",
                "40%",
            )

        with col2:

            st.metric(
                "Aptitude",
                "35%",
            )

        with col3:

            st.metric(
                "Work Style",
                "25%",
            )

    if st.button(
        "✨ Find My Career Directions",
        type="primary",
        use_container_width=True,
    ):

        try:

            generate_career_results()

            st.success(
                "Your personalized career directions are ready! 🎉"
            )

        except Exception as error:

            st.error(
                "Career matching failed."
            )

            st.exception(error)


# ============================================================
# CAREER RESULTS
# ============================================================

if st.session_state.career_results:

    st.divider()

    render_html(
        """
        <div class="section-label">
            YOUR TOP MATCHES
        </div>

        <div class="section-title">
            🏆 Career directions worth exploring
        </div>

        <div class="section-description">
            These are recommendation signals based on your
            current assessment profile.
        </div>
        """
    )

    results = (
        st.session_state.career_results
    )
    
    
    
    # --------------------------------------------------------
    # TOP CAREER HERO
    # --------------------------------------------------------

    top_result = results[0]
    top_explanation = st.session_state.career_explanations[0]

    match_score = round(top_result["overall_match"])

    skill_gap = top_explanation.get("skill_gap")

    if skill_gap is not None:
        readiness_score = round(skill_gap["readiness"])
    else:
        readiness_score = max(
            35,
            min(100, match_score - 18),
        )
    # Use Quick Skill Check when the student has completed it.
    if "quick_readiness" in st.session_state:
        readiness_score = st.session_state.quick_readiness

    render_html(
        f"""
        <div class="hero" style="margin-top:1.2rem;">

            <div class="hero-badge">
                ✨ YOUR STRONGEST CAREER DIRECTION
            </div>

            <div class="hero-title">
                {top_result["career_name"]}
            </div>

            <div class="hero-text">
                {top_result["domain"]}
            </div>

            <div style="
                display:flex;
                gap:3rem;
                flex-wrap:wrap;
                margin-top:1.8rem;
            ">

                <div>
                    <div style="
                        font-family:'Fraunces', Georgia, serif;
                        font-size:2.2rem;
                        font-weight:600;
                    ">
                        {match_score}%
                    </div>

                    <div style="
                        color:#C9D0CA;
                        font-size:0.8rem;
                    ">
                        Career Match
                    </div>
                </div>

                <div>
                    <div style="
                        font-family:'Fraunces', Georgia, serif;
                        font-size:2.2rem;
                        font-weight:600;
                    ">
                        {readiness_score}%
                    </div>

                    <div style="
                        color:#C9D0CA;
                        font-size:0.8rem;
                    ">
                        Current Readiness
                    </div>
                </div>

            </div>

        </div>
        """
    )

    st.progress(
        readiness_score / 100,
    )

    st.caption(
        "Career Match reflects how closely your profile aligns "
        "with the career. Readiness reflects the skill evidence "
        "currently available."
    )

    # --------------------------------------------------------
    # CAREER CARDS
    # --------------------------------------------------------

    for row_start in range(
        0,
        len(results),
        3,
    ):

        row_results = results[
            row_start:
            row_start + 3
        ]

        cols = st.columns(
            len(row_results)
        )

        for index, (
            col,
            result,
        ) in enumerate(
            zip(
                cols,
                row_results,
            ),
            start=row_start + 1,
        ):

            with col:

                render_html(
                    f"""
                    <div class="career-card">

                        <div class="career-rank">
                            #{index} CAREER DIRECTION
                        </div>

                        <div class="career-name">
                            {result['career_name']}
                        </div>

                        <div class="career-domain">
                            {result['domain']}
                        </div>

                        <div class="match-score">
                            {result['overall_match']:.2f}%
                        </div>

                        <div class="match-label">
                            {result['recommendation']}
                        </div>

                    </div>
                    """
                )


    # --------------------------------------------------------
    # DETAILS
    # --------------------------------------------------------

    st.divider()

    render_html(
        """
        <div class="section-title">
            🔎 Explore your matches
        </div>
        """
    )

    explanations = (
        st.session_state.career_explanations
    )

    for index, explanation in enumerate(
        explanations,
        start=1,
    ):

        with st.expander(
            (
                f"#{index}  "
                f"{explanation['career_name']}  ·  "
                f"{explanation['match_score']:.2f}%"
            ),
            expanded=(
                index == 1
            ),
        ):

            # ------------------------------------------------
            # RESULT BANNER
            # ------------------------------------------------

            render_html(
                f"""
                <div class="result-banner">

                    <div class="career-rank">
                        CAREER DIRECTION
                    </div>

                    <h2>
                        {explanation['career_name']}
                    </h2>

                    <p>
                        {explanation['domain']}
                    </p>

                </div>
                """
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Match Score",
                    f"{explanation['match_score']:.2f}%",
                )

            with col2:

                st.metric(
                    "Recommendation",
                    explanation[
                        "recommendation"
                    ],
                )

            # ------------------------------------------------
            # SUMMARY
            # ------------------------------------------------

            st.markdown(
                "### 💡 Why this may suit you"
            )

            st.write(
                explanation[
                    "summary"
                ]
            )

            strengths = explanation[
                "why_this_may_suit_you"
            ]

            if strengths:

                for item in strengths:

                    st.write(
                        f"✓ {item['text']}"
                    )

            # ------------------------------------------------
            # GROWTH
            # ------------------------------------------------

            growth = explanation[
                "growth_opportunities"
            ]

            if growth:

                st.markdown(
                    "### 📈 Areas to develop"
                )

                for item in growth:

                    st.write(
                        f"• **{item['display_name']}** "
                        f"— {item['priority']}"
                    )

                    st.caption(
                        item["text"]
                    )

            # ------------------------------------------------
            # EVIDENCE
            # ------------------------------------------------

            st.markdown(
                "### 📋 Evidence"
            )

            st.info(
                explanation[
                    "evidence_message"
                ]
            )

            # ------------------------------------------------
            # CORE SKILLS
            # ------------------------------------------------

            core_skills = explanation[
                "core_skills"
            ]

            if core_skills:

                st.markdown(
                    "### 🛠️ Core skills"
                )

                skill_cols = st.columns(3)

                for skill_index, skill in enumerate(
                    core_skills
                ):

                    with skill_cols[
                        skill_index % 3
                    ]:

                        render_html(
                            f"""
                            <div class="soft-card">
                                {skill}
                            </div>
                            """
                        )

            # ------------------------------------------------
            # EDUCATION
            # ------------------------------------------------

            st.markdown(
                "### 🎓 Education / pathway"
            )

            st.write(
                explanation[
                    "education_notes"
                ]
            )

            # ------------------------------------------------
            # SKILL GAP
            # ------------------------------------------------

            skill_gap = explanation[
                "skill_gap"
            ]

            if skill_gap is not None:

                st.divider()

                st.markdown(
                    "### 🧩 Skill readiness"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Readiness",
                        f"{skill_gap['readiness']:.1f}%",
                    )

                with col2:

                    st.metric(
                        "Evidence Coverage",
                        f"{skill_gap['evidence_coverage']:.1f}%",
                    )

                st.progress(
                    min(
                        max(
                            skill_gap[
                                "readiness"
                            ] / 100,
                            0.0,
                        ),
                        1.0,
                    )
                )

                unknown = skill_gap[
                    "needs_more_information"
                ]

                if unknown:

                    st.warning(
                        "Some skills still need more "
                        "information before the system "
                        "can accurately identify "
                        "development gaps."
                    )

                    with st.expander(
                        "Skills needing more information"
                    ):

                        for item in unknown:

                            st.write(
                                "• "
                                + readable_name(
                                    item["skill_id"]
                                )
                            )

            # ------------------------------------------------
            # ROADMAP
            # ------------------------------------------------

            roadmap = explanation.get(
                "roadmap"
            )

            if roadmap is not None:

                st.divider()

                st.markdown(
                    "### 🗺️ Personalized roadmap"
                )

                starting_stage = roadmap[
                    "starting_stage"
                ]

                if starting_stage:

                    render_html(
                        f"""
                        <div class="roadmap-start">

                            <div class="roadmap-label">
                                🎯 START NOW
                            </div>

                            <h3>
                                {starting_stage['title']}
                            </h3>

                            <p>
                                {starting_stage['summary']}
                            </p>

                        </div>
                        """
                    )

                    practice = starting_stage.get(
                        "practice",
                        [],
                    )

                    if practice:

                        st.write(
                            "**Practice:**"
                        )

                        for item in practice:

                            st.write(
                                f"• {item}"
                            )

                next_stage = roadmap[
                    "next_stage"
                ]

                if next_stage:

                    render_html(
                        f"""
                        <div class="roadmap-next">

                            <div class="roadmap-label">
                                ➡️ NEXT
                            </div>

                            <h3>
                                {next_stage['title']}
                            </h3>

                            <p>
                                {next_stage['summary']}
                            </p>

                        </div>
                        """
                    )

                later_stages = roadmap[
                    "later_stages"
                ]

                if later_stages:

                    render_html(
                        """
                        <div class="roadmap-later">

                            <div class="roadmap-label">
                                🔭 LATER
                            </div>

                        </div>
                        """
                    )

                    for stage in later_stages:

                        st.write(
                            f"• {stage['title']}"
                        )


# ============================================================
# FINAL MESSAGE
# ============================================================
# ============================================================
# QUICK SKILL CHECK
# ============================================================

if st.session_state.career_results:

    st.markdown(
        "### ⚡ Quick Skill Check"
    )

    st.write(
        "Want a more accurate readiness score? "
        "Tell us how familiar you are with a few "
        "skills related to your top career."
    )

    top_career_id = (
        st.session_state.career_results[0]
        .get("career_id")
    )

    top_career_name = (
        st.session_state.career_results[0]
        .get("career_name")
    )

    career_skill_map = {
        "software_developer": [
            "Programming",
            "Data Structures & Algorithms",
            "Object-Oriented Programming",
            "SQL / Databases",
            "Git / Version Control",
        ],

        "data_analyst": [
            "Excel / Spreadsheets",
            "SQL",
            "Statistics",
            "Data Cleaning",
            "Data Visualization",
        ],

        "data_scientist": [
            "Python",
            "Statistics",
            "SQL",
            "Pandas",
            "Machine Learning",
        ],

        "cybersecurity_analyst": [
            "Networking",
            "Operating Systems",
            "Linux",
            "Cybersecurity Fundamentals",
            "Security Monitoring",
        ],

        "web_developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "Git",
            "APIs",
        ],

        "ui_ux_designer": [
            "User Research",
            "Wireframing",
            "Prototyping",
            "Visual Design",
            "Design Tools",
        ],

        "doctor": [
            "Biology",
            "Chemistry",
            "Anatomy",
            "Physiology",
            "Clinical Reasoning",
        ],

        "nurse": [
            "Biology",
            "Anatomy",
            "Patient Care",
            "Patient Communication",
            "Clinical Skills",
        ],

        "lawyer": [
            "Legal Reasoning",
            "Legal Research",
            "Writing",
            "Verbal Communication",
            "Critical Thinking",
        ],
    }

    quick_skills = career_skill_map.get(
        top_career_id,
        [],
    )

    if quick_skills:

        st.caption(
            f"Top career: {top_career_name}"
        )

        skill_levels = [
            "Never used",
            "Beginner",
            "Intermediate",
            "Advanced",
        ]

        quick_skill_answers = {}

        for index, skill in enumerate(
            quick_skills
        ):

            quick_skill_answers[skill] = (
                st.selectbox(
                    skill,
                    skill_levels,
                    key=f"quick_skill_{index}",
                )
            )

        if st.button(
            "📊 Update My Readiness",
            type="primary",
            use_container_width=True,
        ):

            level_values = {
                "Never used": 0,
                "Beginner": 1,
                "Intermediate": 2,
                "Advanced": 3,
            }

            total = 0

            for answer in quick_skill_answers.values():

                total += level_values[
                    answer
                ]

            quick_readiness = round(
                (
                    total
                    / (
                        len(quick_skills)
                        * 3
                    )
                )
                * 100
            )

            st.session_state.quick_skill_check = (
                quick_skill_answers
            )

            st.session_state.quick_readiness = (
                quick_readiness
            )

            st.success(
                f"Your updated current readiness is "
                f"{quick_readiness}%."
            )

            st.info(
                "Your Career Match stays unchanged. "
                "This check only improves the estimate "
                "of your current skill readiness."
            )

if st.session_state.career_results:

    render_html(
        """
        <div class="card">

            <h3>
                🌱 Keep exploring
            </h3>

            <p>
                Your results are meant to help you understand
                possible directions and identify what to learn
                next. They are recommendation signals, not a
                final decision about your future.
            </p>

        </div>
        """
    )


# ============================================================
# FOOTER
# ============================================================

render_html(
    """
    <div class="footer">
        Student Career Navigator ·
        Career guidance based on assessment signals,
        not career decisions.
    </div>
    """
)
