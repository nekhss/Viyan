from data_loader import load_satellites
from collision import detect_future_conjunctions
from features import extract_features
from risk import assess_risk
from negotiation import negotiate
from decision import make_decision

satellites = load_satellites(
    "stations",
    force_refresh=True
)

conjunctions = detect_future_conjunctions(satellites)

features = extract_features(conjunctions[0])

risk = assess_risk(features)

negotiation = negotiate(features, risk)


decision = make_decision(
    features,
    risk,
    negotiation
)
print("\n=== RISK ===")
print(risk)

print("\n=== NEGOTIATION ===")
print(negotiation)

print("\n=== DECISION ===")
print(decision)

from explanation import generate_explanation

explanation = generate_explanation(
    features,
    risk,
    negotiation,
    decision
)

print("\n=== EXPLANATION ===")
print(explanation["explanation"])