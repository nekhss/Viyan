from pydantic import BaseModel


class AgentLogCreate(BaseModel):
    simulation_id: int
    agent_name: str
    action: str
    message: str | None = None


class AgentLogResponse(BaseModel):
    id: int
    simulation_id: int
    agent_name: str
    action: str
    message: str | None

    class Config:
        from_attributes = True
