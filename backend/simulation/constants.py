"""
Global constants used across the simulation module.
"""

# Mission Priorities
MISSION_PRIORITY = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4
}

# Risk Levels
RISK_LEVELS = [
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
]

# Decision Thresholds
COLLISION_THRESHOLD = 0.70
HIGH_RISK_THRESHOLD = 0.85

# Human Approval Threshold
HUMAN_APPROVAL_CONFIDENCE = 0.80

# Negotiation Status
NEGOTIATION_STATUS = [
    "STARTED",
    "PROPOSED",
    "COUNTERED",
    "ACCEPTED",
    "REJECTED",
    "COMPLETED"
]