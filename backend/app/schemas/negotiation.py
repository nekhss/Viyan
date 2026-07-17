from pydantic import BaseModel


class NegotiationCreate(BaseModel):
    simulation_id: int
    status: str = "ONGOING"
    final_decision: str | None = None


class NegotiationResponse(BaseModel):
    id: int
    simulation_id: int
    status: str
    final_decision: str | None

    class Config:
        from_attributes = True
