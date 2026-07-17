"""
Pydantic models for the VIYAN Simulation Engine.
"""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class MissionPriority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class NegotiationStatus(str, Enum):
    STARTED = "STARTED"
    PROPOSED = "PROPOSED"
    COUNTERED = "COUNTERED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    COMPLETED = "COMPLETED"


class Satellite(BaseModel):
    id: str
    name: str

    fuel: float = Field(..., ge=0, le=100)

    mission_priority: MissionPriority

    mission_type: str

    tle_line1: str
    tle_line2: str


class OrbitState(BaseModel):
    latitude: float
    longitude: float
    altitude_km: float

    velocity_kms: float

    timestamp: str


class CollisionEvent(BaseModel):
    satellite_1: str
    satellite_2: str

    collision_probability: float = Field(..., ge=0, le=1)

    minimum_distance_km: float

    time_to_collision_minutes: float


class RiskAssessment(BaseModel):
    collision_probability: float

    predicted_risk: str

    confidence: float

    shap_summary: List[str]


class NegotiationProposal(BaseModel):
    proposer: str

    maneuver: str

    fuel_cost: float

    mission_impact: str


class Decision(BaseModel):
    approved: bool

    final_maneuver: str

    reasoning: str

    human_approval_required: bool


class TimelineEvent(BaseModel):
    timestamp: str

    event: str

    details: str


class SimulationResult(BaseModel):
    satellites: List[Satellite]

    collision: CollisionEvent

    risk: RiskAssessment

    proposals: List[NegotiationProposal]

    decision: Decision

    timeline: List[TimelineEvent]