from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.mission import Mission
from app.schemas.mission import MissionCreate, MissionResponse


router = APIRouter(prefix="/missions", tags=["Missions"])


@router.post("/", response_model=MissionResponse)
def create_mission(mission: MissionCreate, db: Session = Depends(get_db)):
    new_mission = Mission(name=mission.name, description=mission.description)

    db.add(new_mission)
    db.commit()
    db.refresh(new_mission)

    return new_mission


@router.get("/", response_model=list[MissionResponse])
def get_missions(db: Session = Depends(get_db)):
    return db.query(Mission).all()
