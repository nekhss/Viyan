from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.agent_log import AgentLog
from app.schemas.agent_log import AgentLogCreate, AgentLogResponse


router = APIRouter(prefix="/agent-logs", tags=["Agent Logs"])


@router.post("/", response_model=AgentLogResponse)
def create_agent_log(log: AgentLogCreate, db: Session = Depends(get_db)):
    new_log = AgentLog(
        simulation_id=log.simulation_id,
        agent_name=log.agent_name,
        action=log.action,
        message=log.message,
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log


@router.get("/", response_model=list[AgentLogResponse])
def get_agent_logs(db: Session = Depends(get_db)):
    return db.query(AgentLog).all()
