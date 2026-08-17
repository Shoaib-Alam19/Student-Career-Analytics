import streamlit as st
import sys
import pandas as pd
import plotly.express as px

sys.path.append("src")

from predict import analyze_student


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Career Analytics",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666666;
        margin-bottom: 35px;
    }

    .section-title {
        font-size: 26px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .analyze-button-title {
        text-align: center;
        font-size: 18px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎓 Student Career Analytics</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze your career readiness and get a placement prediction.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# STUDENT INPUT SECTION
# ============================================================

st.header("Enter Your Profile")

input_col1, input_col2 = st.columns(2)


# ============================================================
# ACADEMIC & APTITUDE
# ============================================================

with input_col1:

    st.markdown(
        '<div class="section-title">'
        '📚 Academic & Aptitude'
        '</div>',
        unsafe_allow_html=True
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.0,
        step=0.1
    )

    ssc_marks = st.number_input(
        "SSC Marks",
        min_value=0,
        max_value=100,
        value=70,
        step=1
    )

    hsc_marks = st.number_input(
        "HSC Marks",
        min_value=0,
        max_value=100,
        value=70,
        step=1
    )

    aptitude = st.number_input(
        "Aptitude Test Score",
        min_value=0,
        max_value=100,
        value=70,
        step=1
    )

    soft_skills = st.number_input(
        "Soft Skills Rating",
        min_value=0.0,
        max_value=5.0,
        value=3.0,
        step=0.1
    )


# ============================================================
# EXPERIENCE & ACTIVITIES
# ============================================================

with input_col2:

    st.markdown(
        '<div class="section-title">'
        '💼 Experience & Activities'
        '</div>',
        unsafe_allow_html=True
    )

    internships = st.number_input(
        "Internships",
        min_value=0,
        max_value=2,
        value=0,
        step=1
    )

    projects = st.number_input(
        "Projects",
        min_value=0,
        max_value=3,
        value=1,
        step=1
    )

    workshops = st.number_input(
        "Workshops / Certifications",
        min_value=0,
        max_value=3,
        value=1,
        step=1
    )

    extracurricular = st.selectbox(
        "Extracurricular Activities",
        ["Yes", "No"]
    )

    placement_training = st.selectbox(
        "Placement Training",
        ["Yes", "No"]
    )


# ============================================================
# ANALYZE BUTTON
# ============================================================

st.divider()

st.markdown(
    '<div class="analyze-button-title">'
    'Ready to analyze your profile?'
    '</div>',
    unsafe_allow_html=True
)

button_col1, button_col2 = st.columns(2)

with button_col1:

    analyze_button = st.button(
        "🔍 Analyze My Profile",
        use_container_width=True
    )

with button_col2:

    reset_button = st.button(
        "🔄 Reset Profile",
        use_container_width=True
    )


if reset_button:

    st.rerun()


# ============================================================
# ANALYSIS
# ============================================================

if analyze_button:

    # --------------------------------------------------------
    # Create Student Profile
    # --------------------------------------------------------

    student = {
        "CGPA": cgpa,
        "Internships": internships,
        "Projects": projects,
        "Workshops/Certifications": workshops,
        "AptitudeTestScore": aptitude,
        "SoftSkillsRating": soft_skills,
        "ExtracurricularActivities": extracurricular,
        "PlacementTraining": placement_training,
        "SSC_Marks": ssc_marks,
        "HSC_Marks": hsc_marks
    }


    # --------------------------------------------------------
    # Run Analysis
    # --------------------------------------------------------

    result = analyze_student(student)

    readiness = result["readiness"]


    # ========================================================
    # MAIN RESULTS
    # ========================================================

    result_col1, result_col2, result_col3 = st.columns(3)


    # --------------------------------------------------------
    # PLACEMENT PREDICTION
    # --------------------------------------------------------

    with result_col1:

        st.subheader("🎯 Placement")

        if result["placement_prediction"] == "Placed":

            st.success("✅ Placed")

        else:

            st.warning("⚠️ Not Placed")


    # --------------------------------------------------------
    # READINESS SCORE
    # --------------------------------------------------------

    with result_col2:

        st.subheader("📊 Readiness")

        st.metric(
            "Score",
            f'{readiness["score"]} / 100'
        )

        st.progress(
            int(readiness["score"]) / 100
        )


    # --------------------------------------------------------
    # READINESS LEVEL
    # --------------------------------------------------------

    with result_col3:

        st.subheader("🏆 Level")

        st.metric(
            "Career Readiness",
            readiness["level"]
        )


    # ========================================================
    # READINESS BREAKDOWN
    # ========================================================

    st.subheader("📈 Readiness Breakdown")

    breakdown_col1, breakdown_col2, breakdown_col3, breakdown_col4, breakdown_col5 = st.columns(5)


    # Academic
    with breakdown_col1:

        st.metric(
            "Academic",
            f'{readiness["academic"]} / 25'
        )

        st.progress(
            readiness["academic"] / 25
        )


    # Technical
    with breakdown_col2:

        st.metric(
            "Technical",
            f'{readiness["technical"]} / 30'
        )

        st.progress(
            readiness["technical"] / 30
        )


    # Aptitude
    with breakdown_col3:

        st.metric(
            "Aptitude",
            f'{readiness["aptitude"]} / 15'
        )

        st.progress(
            readiness["aptitude"] / 15
        )


    # Experience
    with breakdown_col4:

        st.metric(
            "Experience",
            f'{readiness["experience"]} / 15'
        )

        st.progress(
            readiness["experience"] / 15
        )


    # Professional
    with breakdown_col5:

        st.metric(
            "Professional",
            f'{readiness["professional"]} / 15'
        )

        st.progress(
            readiness["professional"] / 15
        )


    # ========================================================
    # READINESS CHART
    # ========================================================

    st.subheader("📊 Career Readiness by Category")

    chart_data = pd.DataFrame({

        "Category": [
            "Academic",
            "Technical",
            "Aptitude",
            "Experience",
            "Professional"
        ],

        "Percentage": [
            (readiness["academic"] / 25) * 100,
            (readiness["technical"] / 30) * 100,
            (readiness["aptitude"] / 15) * 100,
            (readiness["experience"] / 15) * 100,
            (readiness["professional"] / 15) * 100
        ]
    })


    # Create Plotly chart

    fig = px.bar(
        chart_data,
        x="Category",
        y="Percentage",
        range_y=[0, 100],
        text="Percentage",
        title="Career Readiness by Category"
    )


    # Percentage labels

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )


    # Chart layout

    fig.update_layout(
        yaxis_title="Readiness (%)",
        xaxis_title="",
        showlegend=False
    )


    # Display chart

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # STRENGTHS
    # ========================================================

    st.subheader("💪 Strengths")

    if result["strengths"]:

        for strength in result["strengths"]:

            st.success(
                f"✓ {strength}"
            )

    else:

        st.info(
            "No major strengths identified yet."
        )


    # ========================================================
    # AREAS TO IMPROVE
    # ========================================================

    st.subheader("⚠️ Areas to Improve")

    if result["weaknesses"]:

        for weakness in result["weaknesses"]:

            st.warning(
                f"⚠ {weakness}"
            )

    else:

        st.success(
            "No major weak areas identified."
        )


    # ========================================================
    # RECOMMENDATIONS
    # ========================================================

    st.subheader("💡 Recommendations")

    if result["recommendations"]:

        for recommendation in result["recommendations"]:

            st.info(
                f"→ {recommendation}"
            )

    else:

        st.success(
            "Your profile looks strong. Keep improving consistently!"
        )

    st.divider()

    st.caption(
        "⚠️ Note: Placement prediction is based on the trained machine "
        "learning model and the information provided. It is an estimate "
        "and does not guarantee actual placement."
    )