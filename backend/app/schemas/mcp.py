from pydantic import BaseModel


class MCPLogCreate(BaseModel):
    tool: str
    request: str | None = None
    response: str | None = None
    status: str = "SUCCESS"


class MCPLogResponse(BaseModel):
    id: int
    tool: str
    request: str | None
    response: str | None
    status: str

    class Config:
        from_attributes = True
