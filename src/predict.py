import joblib
import pandas as pd

from readiness import (
    calculate_readiness,
    analyze_strengths,
    generate_recommendations
)


model = joblib.load("models/placement_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


def analyze_student(student):

    # Convert student dictionary to DataFrame
    student_df = pd.DataFrame([student])

    # Apply the saved preprocessing
    student_processed = preprocessor.transform(student_df)

    # Make placement prediction
    prediction = model.predict(student_processed)

    predicted_status = label_encoder.inverse_transform(
        prediction
    )[0]

    # Calculate career readiness
    readiness_result = calculate_readiness(student)

    # Analyze strengths and weaknesses
    strengths, weaknesses = analyze_strengths(
        readiness_result
    )

    # Generate recommendations
    recommendations = generate_recommendations(
        student,
        weaknesses
    )

    return {
        "placement_prediction": predicted_status,
        "readiness": readiness_result,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }