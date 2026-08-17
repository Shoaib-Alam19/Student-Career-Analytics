# 🎓 Student Career Analytics

A machine learning based web application that analyzes a student's academic, technical, aptitude, experience, and professional profile to predict placement status and calculate a Career Readiness Score.

## 🚀 Features

- Placement prediction using Machine Learning
- Career Readiness Score out of 100
- Readiness level classification
- Academic performance analysis
- Technical/project analysis
- Aptitude analysis
- Internship/experience analysis
- Professional skills analysis
- Strengths identification
- Areas for improvement
- Personalized recommendations
- Interactive career-readiness chart
- Streamlit-based web interface

## 🧠 Machine Learning

The project compares multiple classification models:

- Logistic Regression
- Decision Tree
- Random Forest

### Model Performance

| Model | Accuracy |
|---|---:|
| Logistic Regression | 79.19% |
| Decision Tree | 70.42% |
| Random Forest | 79.54% |

Random Forest achieved the highest accuracy among the tested models.

## 📊 Career Readiness

The Career Readiness Score is calculated using five major categories:

| Category | Maximum Score |
|---|---:|
| Academic | 25 |
| Technical / Projects | 30 |
| Aptitude | 15 |
| Experience | 15 |
| Professional Skills | 15 |
| **Total** | **100** |

### Readiness Levels

| Score | Level |
|---:|---|
| 80–100 | Excellent |
| 70–79.99 | Good |
| 60–69.99 | Developing |
| Below 60 | Needs Improvement |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Joblib

## 📁 Project Structure

```text
Student-Career-Analytics/
│
├── app/
│   └── app.py
│
├── data/
│
├── models/
│   ├── label_encoder.pkl
│   ├── placement_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│
├── src/
│   ├── inspect_data.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── readiness.py
│   └── train_model.py
│
├── .gitignore
├── PROJECT_NOTES.md
├── README.md
└── requirements.txt