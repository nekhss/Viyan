from pydantic import BaseModel


class SimulationCreate(BaseModel):
    simulation_id: str
    collision_probability: float
    risk_prediction: float | None = None
    confidence: float | None = None
    status: str = "PENDING"


class SimulationResponse(BaseModel):
    id: int
    simulation_id: str
    collision_probability: float
    risk_prediction: float | None
    confidence: float | None
    status: str

    class Config:
        from_attributes = True
