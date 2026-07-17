from data_loader import load_satellites
from collision import detect_future_conjunctions
from features import extract_features
from risk import assess_risk
from negotiation import negotiate
from decision import make_decision
from timeline import generate_timeline

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

timeline = generate_timeline(
    features,
    risk,
    negotiation,
    decision
)

print("\n=== TIMELINE ===")

for event in timeline["timeline"]:
    print(event)
    