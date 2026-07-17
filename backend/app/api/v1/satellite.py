from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.satellite import Satellite
from app.schemas.satellite import SatelliteCreate, SatelliteResponse


router = APIRouter(prefix="/satellites", tags=["Satellites"])


@router.post("/", response_model=SatelliteResponse)
def create_satellite(satellite: SatelliteCreate, db: Session = Depends(get_db)):
    new_satellite = Satellite(
        satellite_id=satellite.satellite_id,
        name=satellite.name,
        fuel=satellite.fuel,
        priority=satellite.priority,
        mission=satellite.mission,
        tle=satellite.tle,
        status=satellite.status,
    )

    db.add(new_satellite)
    db.commit()
    db.refresh(new_satellite)

    return new_satellite


@router.get("/", response_model=list[SatelliteResponse])
def get_satellites(db: Session = Depends(get_db)):
    return db.query(Satellite).all()
