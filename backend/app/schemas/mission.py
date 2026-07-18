from pydantic import BaseModel


class MissionCreate(BaseModel):
    name: str
    description: str | None = None


class MissionResponse(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        from_attributes = True
