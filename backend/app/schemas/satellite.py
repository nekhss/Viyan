from pydantic import BaseModel


class SatelliteCreate(BaseModel):
    satellite_id: str
    name: str
    fuel: float
    priority: str
    mission: str
    tle: str
    status: str = "ACTIVE"


class SatelliteResponse(BaseModel):
    id: int
    satellite_id: str
    name: str
    fuel: float
    priority: str
    mission: str
    tle: str
    status: str

    class Config:
        from_attributes = True
