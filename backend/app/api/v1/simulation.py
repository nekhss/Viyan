from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.simulation_session import SimulationSession
from app.schemas.simulation import SimulationCreate, SimulationResponse


router = APIRouter(prefix="/simulation", tags=["Simulation"])


@router.post("/", response_model=SimulationResponse)
def create_simulation(simulation: SimulationCreate, db: Session = Depends(get_db)):
    new_simulation = SimulationSession(
        simulation_id=simulation.simulation_id,
        collision_probability=simulation.collision_probability,
        risk_prediction=simulation.risk_prediction,
        confidence=simulation.confidence,
        status=simulation.status,
    )

    db.add(new_simulation)
    db.commit()
    db.refresh(new_simulation)

    return new_simulation


@router.get("/", response_model=list[SimulationResponse])
def get_simulations(db: Session = Depends(get_db)):
    return db.query(SimulationSession).all()
