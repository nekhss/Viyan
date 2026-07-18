def calculate_risk(collision_probability: float):
    """
    Calculates risk percentage and assigns a status.
    """

    risk_prediction = collision_probability * 100

    if risk_prediction >= 80:
        status = "HIGH_RISK"
    elif risk_prediction >= 50:
        status = "MEDIUM_RISK"
    else:
        status = "LOW_RISK"

    return risk_prediction, status
