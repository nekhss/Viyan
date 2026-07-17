from typing import Dict, List


def generate_timeline(
    features: Dict,
    risk: Dict,
    negotiation: Dict,
    decision: Dict
) -> Dict:
    """
    Generate a chronological mission timeline
    describing the autonomous decision process.
    """

    negotiation = negotiation["negotiation"]
    decision = decision["decision"]

    encounter = features["encounter"]

    timeline: List[Dict] = [

        {
            "step": 1,
            "event": "Conjunction Detected",
            "description":
                (
                    f"Potential conjunction detected between "
                    f"{features['satellite1']['name']} and "
                    f"{features['satellite2']['name']}."
                )
        },

        {
            "step": 2,
            "event": "Risk Assessment",
            "description":
                (
                    f"Encounter classified as "
                    f"{risk['risk_level']} risk "
                    f"(Score: {risk['risk_score']:.3f})."
                )
        },

        {
            "step": 3,
            "event": "Negotiation",
            "description":
                negotiation["reason"]
        }
    ]

    # Decision stage

    if decision["status"] == "NO_ACTION":

        timeline.append({

            "step": 4,

            "event": "Decision",

            "description":
                "No avoidance maneuver required."
        })

    elif decision["status"] == "WAITING_FOR_APPROVAL":

        timeline.append({

            "step": 4,

            "event": "Operator Approval",

            "description":
                "Awaiting operator approval before maneuver execution."
        })

    else:

        timeline.append({

            "step": 4,

            "event": "Decision",

            "description":
                (
                    f"{decision['target_satellite']} will perform a "
                    f"{decision['maneuver']['type']} maneuver "
                    f"of {decision['maneuver']['delta_altitude_km']} km."
                )
        })

        timeline.append({

            "step": 5,

            "event": "Expected Outcome",

            "description":
                (
                    f"Predicted minimum separation: "
                    f"{decision['expected_separation_km']} km."
                )
        })

    return {
        "timeline": timeline
    }