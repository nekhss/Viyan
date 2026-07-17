from typing import Dict


def generate_explanation(
    features: Dict,
    risk: Dict,
    negotiation: Dict,
    decision: Dict
) -> Dict:
    """
    Generate a human-readable explanation of the
    autonomous collision avoidance decision.
    """

    negotiation = negotiation["negotiation"]
    decision = decision["decision"]

    sat1 = features["satellite1"]["name"]
    sat2 = features["satellite2"]["name"]

    risk_level = risk["risk_level"]
    risk_score = risk["risk_score"]

    # -----------------------------
    # No Action
    # -----------------------------
    if decision["status"] == "NO_ACTION":

        explanation = (
            f"A potential conjunction was detected between "
            f"{sat1} and {sat2}. "
            f"The encounter was classified as {risk_level} risk "
            f"(Score: {risk_score:.3f}). "
            f"No avoidance maneuver is required because the risk "
            f"remains within acceptable operational limits."
        )

    # -----------------------------
    # Waiting for approval
    # -----------------------------
    elif decision["status"] == "WAITING_FOR_APPROVAL":

        explanation = (
            f"A potential conjunction was detected between "
            f"{sat1} and {sat2}. "
            f"The encounter was classified as {risk_level} risk "
            f"(Score: {risk_score:.3f}). "
            f"The proposed maneuver requires operator approval "
            f"before execution due to the elevated collision risk."
        )

    # -----------------------------
    # Approved maneuver
    # -----------------------------
    else:

        maneuver = decision["maneuver"]

        explanation = (
            f"A potential conjunction was detected between "
            f"{sat1} and {sat2}. "
            f"The encounter was classified as {risk_level} risk "
            f"(Score: {risk_score:.3f}). "
            f"{negotiation['reason']} "
            f"{decision['target_satellite']} will execute a "
            f"{maneuver['type']} maneuver of "
            f"{maneuver['delta_altitude_km']} km after "
            f"{maneuver['execution_delay_sec']} seconds. "
            f"The maneuver is expected to increase the minimum "
            f"separation to "
            f"{decision['expected_separation_km']} km while "
            f"maintaining {decision['fuel_cost'].lower()} "
            f"fuel consumption."
        )

    return {
        "explanation": explanation
    }