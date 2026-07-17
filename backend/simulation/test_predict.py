from data_loader import load_satellites
from collision import detect_future_conjunctions
from features import extract_features

from ml.predict import predict_collision_probability


satellites = load_satellites(
    "stations",
    force_refresh=True
)

conjunctions = detect_future_conjunctions(satellites)

features = extract_features(conjunctions[0])

probability = predict_collision_probability(features)

print("\n=== ML Prediction ===")
print(probability)