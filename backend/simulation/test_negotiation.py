from data_loader import load_satellites
from trajectory import predict_trajectory
from collision import detect_future_conjunctions
from features import extract_features
from risk import assess_risk
from negotiation import negotiate

satellites = load_satellites(
    "stations",
    force_refresh=True
)

conjunctions = detect_future_conjunctions(satellites)

first = conjunctions[0]

features = extract_features(first)
risk = assess_risk(features)

result = negotiate(features, risk)

print("\n=== NEGOTIATION ===")
print(result)