from pathlib import Path

import joblib
import shap
import explanation
from ml.preprocessing import prepare_features


BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "model.pkl"

model = joblib.load(MODEL_PATH)

explainer = shap.Explainer(model)


def explain_prediction(features):

    X = prepare_features(features)

    explanation = explainer(X)
    print("SHAP Shape:", explanation.values.shape)
    print(explanation.values)
    values = explanation.values[0, :, 1]
    result = []

    for feature, impact in zip(X.columns, values):

        result.append({
            "feature": feature,
            "impact": round(float(impact), 4)
        })

    result.sort(
        key=lambda x: abs(x["impact"]),
        reverse=True
    )

    return result

def generate_reasoning(explanation):

    reasons = []

    for item in explanation:

        if abs(item["impact"]) < 0.01:
            continue

        feature = item["feature"]

        if feature == "closest_distance_km":
            reasons.append("Very close separation")

        elif feature == "relative_velocity_km_s":
            reasons.append("High relative velocity")

        elif feature == "time_to_closest_sec":
            reasons.append("Immediate encounter")

        elif feature == "priority_difference":
            reasons.append("Large mission priority difference")

        elif feature == "altitude_difference_km":
            reasons.append("Small altitude separation")

    return reasons