from data_loader import load_satellites
from collision import detect_future_conjunctions
from features import extract_features
from risk import assess_risk

satellites = load_satellites("stations")

alerts = detect_future_conjunctions(satellites)

if alerts:
    features = extract_features(alerts[0])
    risk = assess_risk(features)

    print("=== FEATURES ===")
    print(features)

    print("\n=== RISK ===")
    print(risk)

from ml.shap_explainer import explain_prediction,generate_reasoning

explanation = explain_prediction(features)

print(explanation)

reasons = generate_reasoning(explanation)

print("\n=== REASONS ===")
print(reasons)