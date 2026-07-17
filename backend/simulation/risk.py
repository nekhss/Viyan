"""
Risk assessment engine.
"""

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
    Compute collision risk from extracted features.
    """

    encounter = features["encounter"]

    sat1 = features["satellite1"]
    sat2 = features["satellite2"]

    # -----------------------------
    # Distance Score
    # -----------------------------
    # Smaller distance => Higher risk

    distance_score = 1 - normalize(
        encounter["closest_distance_km"],
        0,
        5
    )

    # -----------------------------
    # Relative Velocity Score
    # -----------------------------

    velocity_score = normalize(
        encounter["relative_velocity_km_s"],
        0,
        15
    )

    # -----------------------------
    # Time Score
    # -----------------------------
    # Less time => Higher urgency

    time_score = 1 - normalize(
        encounter["time_to_closest_sec"],
        0,
        1800
    )

    # -----------------------------
    # Mission Priority
    # -----------------------------

    priority_score = max(
        sat1["priority"],
        sat2["priority"]
    ) / 10

    # -----------------------------
    # Weighted Risk
    # -----------------------------

    risk_score = (

        0.45 * distance_score +

        0.20 * velocity_score +

        0.20 * time_score +

        0.15 * priority_score

    )

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

        "risk_level": level,

        "recommended_action": action,

        "requires_negotiation": level == "HIGH"

    }