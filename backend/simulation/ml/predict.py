from pathlib import Path
from typing import Dict

import joblib

try:
    from preprocessing import prepare_features
except ImportError:
    from .preprocessing import prepare_features


BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "model.pkl"


# Load once when the module is imported.
model = joblib.load(MODEL_PATH)


def predict_collision_probability(features: Dict) -> float:
    """
    Predict the probability of collision for an encounter.
    """

    X = prepare_features(features)

    probability = model.predict_proba(X)[0][1]

    return round(float(probability), 4)