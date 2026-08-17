import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from preprocess import prepare_data


# Prepare the data
(
    X_train_processed,
    X_test_processed,
    y_train_encoded,
    y_test_encoded,
    preprocessor,
    label_encoder
) = prepare_data()


# Create models
logistic_model = LogisticRegression(max_iter=1000)

tree_model = DecisionTreeClassifier(
    random_state=42
)

forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train models
logistic_model.fit(
    X_train_processed,
    y_train_encoded
)

tree_model.fit(
    X_train_processed,
    y_train_encoded
)

forest_model.fit(
    X_train_processed,
    y_train_encoded
)


print("All models trained successfully!")


# Make predictions
logistic_pred = logistic_model.predict(X_test_processed)
tree_pred = tree_model.predict(X_test_processed)
forest_pred = forest_model.predict(X_test_processed)

print("Model predictions generated successfully!")


# Calculate accuracy
logistic_accuracy = accuracy_score(
    y_test_encoded,
    logistic_pred
)

tree_accuracy = accuracy_score(
    y_test_encoded,
    tree_pred
)

forest_accuracy = accuracy_score(
    y_test_encoded,
    forest_pred
)


# Compare models
print("\n===== MODEL COMPARISON =====")
print(
    "Logistic Regression:",
    logistic_accuracy * 100
)
print(
    "Decision Tree:",
    tree_accuracy * 100
)
print(
    "Random Forest:",
    forest_accuracy * 100
)

joblib.dump(forest_model, "models/placement_model.pkl")
joblib.dump(preprocessor, "models/preprocessor.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")