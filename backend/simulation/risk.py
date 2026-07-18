"""
Risk assessment engine.
"""

from simulation.ml.predict import predict_collision_probability
from simulation.known_relationships import is_expected_proximity


def normalize(value, minimum, maximum):
    """
    Normalize a value to the range [0, 1].
    """

    if maximum == minimum:
        return 0.0

    value = max(minimum, min(value, maximum))

    return (value - minimum) / (maximum - minimum)


def assess_risk(features):
    """
    Compute collision risk using both
    rule-based scoring and ML prediction.
    """

    encounter = features["encounter"]

    sat1 = features["satellite1"]
    sat2 = features["satellite2"]

    # -----------------------------
    # Rule-Based Scores
    # -----------------------------
    if is_expected_proximity(sat1["name"], sat2["name"]):
        return {
            "risk_score": 0.0,
            "rule_score": 0.0,
            "ml_probability": 0.0,
            "risk_level": "EXPECTED_PROXIMITY",
            "recommended_action": "NONE",
            "requires_negotiation": False,
            "notes": ("Satellites are known to be docked or operating together."),
        }
    distance_score = 1 - normalize(encounter["closest_distance_km"], 0, 5)

    velocity_score = normalize(encounter["relative_velocity_km_s"], 0, 15)

    time_score = 1 - normalize(encounter["time_to_closest_sec"], 0, 1800)

    priority_score = max(sat1["priority"], sat2["priority"]) / 10

    # -----------------------------
    # Rule-Based Risk
    # -----------------------------

    rule_score = (
        0.40 * distance_score
        + 0.20 * velocity_score
        + 0.20 * time_score
        + 0.20 * priority_score
    )

    # -----------------------------
    # ML Prediction
    # -----------------------------

    ml_probability = predict_collision_probability(features)

    # -----------------------------
    # Hybrid Risk Score
    # -----------------------------

    risk_score = 0.55 * rule_score + 0.45 * ml_probability

    # -----------------------------
    # Classification
    # -----------------------------

    if risk_score >= 0.75:
        level = "HIGH"

        action = "NEGOTIATE"

    elif risk_score >= 0.45:
        level = "MEDIUM"

        action = "MONITOR"

    else:
        level = "LOW"

        action = "IGNORE"

    return {
        "risk_score": round(risk_score, 3),
        "rule_score": round(rule_score, 3),
        "ml_probability": round(ml_probability, 3),
        "risk_level": level,
        "recommended_action": action,
        "requires_negotiation": level == "HIGH",
    }
