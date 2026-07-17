from typing import Dict


def negotiate(features: Dict, risk: Dict) -> Dict:
    """
    Decide which satellite should perform the avoidance maneuver.
    """

    sat1 = features["satellite1"]
    sat2 = features["satellite2"]

    p1 = sat1["priority"]
    p2 = sat2["priority"]

    # Low-risk encounters require no negotiation.
    if risk["risk_level"] == "LOW":
        return {
    "negotiation": {
        "status": "SKIPPED",
        "resolution_method": "NO_NEGOTIATION",
        "winner": None,
        "yielding_satellite": None,
        "reason": "Risk level is LOW. No negotiation required.",
        "confidence": 1.0,
        "requires_operator_approval": False
    }
}

    # Higher-priority satellite keeps its trajectory.
    if p1 > p2:
        winner = sat1["name"]
        yielding = sat2["name"]
        reason = f"{winner} has higher mission priority."

    elif p2 > p1:
        winner = sat2["name"]
        yielding = sat1["name"]
        reason = f"{winner} has higher mission priority."

    else:
        winner = "SHARED"
        yielding = "BOTH"
        reason = "Both satellites have equal priority."

    # Confidence based on priority difference.
    if winner == "SHARED":
        confidence = 0.50
    else:
        diff = abs(p1 - p2)

        if diff >= 5:
            confidence = 0.98
        elif diff >= 3:
            confidence = 0.90
        elif diff >= 1:
            confidence = 0.75
        else:
            confidence = 0.60

    requires_operator_approval = risk["risk_score"] >= 0.90
    
    return {
    "negotiation": {
        "status": "SUCCESS",
        "resolution_method": "PRIORITY_BASED" if winner != "SHARED" else "SHARED_RESPONSIBILITY",
        "winner": winner,
        "yielding_satellite": yielding,
        "reason": reason,
        "confidence": round(confidence, 2),
        "requires_operator_approval": requires_operator_approval
    }
}