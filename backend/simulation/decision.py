from typing import Dict


DEFAULT_MANEUVER_DELAY_SEC = 300


def make_decision(
    features: Dict,
    risk: Dict,
    negotiation: Dict
) -> Dict:
    """
    Decide the avoidance maneuver based on
    risk assessment and negotiation outcome.
    """

    negotiation = negotiation["negotiation"]

    # No maneuver needed.
    if negotiation["status"] == "SKIPPED":

        return {
            "decision": {
                "status": "NO_ACTION",

                "target_satellite": None,

                "maneuver": {
                    "type": None,
                    "delta_altitude_km": 0,
                    "execution_delay_sec": 0
                },

                "expected_separation_km": round(
                    features["encounter"]["closest_distance_km"], 2
                ),

                "fuel_cost": "NONE",

                "decision_confidence": 1.0
            }
        }

    # Wait for operator approval.
    if negotiation["requires_operator_approval"]:

        return {
            "decision": {
                "status": "WAITING_FOR_APPROVAL",

                "target_satellite": negotiation["yielding_satellite"],

                "maneuver": {
                    "type": None,
                    "delta_altitude_km": None,
                    "execution_delay_sec": None
                },

                "expected_separation_km": None,

                "fuel_cost": None,

                "decision_confidence": negotiation["confidence"]
            }
        }

    # Determine maneuver based on risk level.
    if risk["risk_level"] == "MEDIUM":

        maneuver_type = "RAISE_ORBIT"
        delta_altitude = 2.0
        fuel_cost = "LOW"

        expected_separation = max(
            features["encounter"]["closest_distance_km"] + 5.0,
            5.0
        )

    else:  # HIGH risk

        maneuver_type = "LOWER_ORBIT"
        delta_altitude = 5.0
        fuel_cost = "MEDIUM"

        expected_separation = max(
            features["encounter"]["closest_distance_km"] + 10.0,
            10.0
        )

    return {
        "decision": {
            "status": "APPROVED",

            "target_satellite": negotiation["yielding_satellite"],

            "maneuver": {
                "type": maneuver_type,
                "delta_altitude_km": delta_altitude,
                "execution_delay_sec": DEFAULT_MANEUVER_DELAY_SEC
            },

            "expected_separation_km": round(
                expected_separation,
                2
            ),

            "fuel_cost": fuel_cost,

            "decision_confidence": negotiation["confidence"]
        }
    }