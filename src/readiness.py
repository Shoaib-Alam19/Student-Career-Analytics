def calculate_readiness(student):
    # 1. Academic Performance — 25 points
    cgpa_score = (student["CGPA"] / 10) * 10
    ssc_score = (student["SSC_Marks"] / 100) * 7.5
    hsc_score = (student["HSC_Marks"] / 100) * 7.5

    academic_score = cgpa_score + ssc_score + hsc_score

    # 2. Technical / Projects — 30 points
    project_score = (student["Projects"] / 3) * 20
    workshop_score = (
        student["Workshops/Certifications"] / 3
    ) * 10

    technical_score = project_score + workshop_score

    # 3. Aptitude — 15 points
    aptitude_score = (
        student["AptitudeTestScore"] / 100
    ) * 15

    # 4. Experience — 15 points
    experience_score = (
        student["Internships"] / 2
    ) * 15

    # 5. Professional Skills — 15 points
    soft_skill_score = (
        student["SoftSkillsRating"] / 5
    ) * 7

    extracurricular_score = (
        4
        if student["ExtracurricularActivities"] == "Yes"
        else 0
    )

    training_score = (
        4
        if student["PlacementTraining"] == "Yes"
        else 0
    )

    professional_score = (
        soft_skill_score
        + extracurricular_score
        + training_score
    )

    # Total score
    total_score = (
        academic_score
        + technical_score
        + aptitude_score
        + experience_score
        + professional_score
    )

    # Readiness level
    if total_score >= 80:
        level = "Excellent"
    elif total_score >= 70:
        level = "Good"
    elif total_score >= 60:
        level = "Developing"
    else:
        level = "Needs Improvement"

    return {
        "score": round(total_score, 2),
        "level": level,
        "academic": round(academic_score, 2),
        "technical": round(technical_score, 2),
        "aptitude": round(aptitude_score, 2),
        "experience": round(experience_score, 2),
        "professional": round(professional_score, 2)
    }


def analyze_strengths(result):
    categories = {
        "Academic": (result["academic"], 25),
        "Technical/Projects": (result["technical"], 30),
        "Aptitude": (result["aptitude"], 15),
        "Experience": (result["experience"], 15),
        "Professional Skills": (result["professional"], 15)
    }

    strengths = []
    weaknesses = []

    for category, (score, maximum) in categories.items():
        percentage = (score / maximum) * 100

        if percentage >= 75:
            strengths.append(category)
        elif percentage < 60:
            weaknesses.append(category)

    return strengths, weaknesses


def generate_recommendations(student, weaknesses):
    recommendations = []

    if "Experience" in weaknesses:
        recommendations.append(
            "Try to gain internship or practical industry experience."
        )

    if "Technical/Projects" in weaknesses:
        recommendations.append(
            "Build more practical projects and strengthen technical skills."
        )

    if "Aptitude" in weaknesses:
        recommendations.append(
            "Practice quantitative aptitude, logical reasoning, and placement tests."
        )

    if "Academic" in weaknesses:
        recommendations.append(
            "Focus on improving CGPA and academic performance."
        )

    if "Professional Skills" in weaknesses:
        recommendations.append(
            "Improve soft skills, extracurricular involvement, and placement preparation."
        )

    return recommendations


