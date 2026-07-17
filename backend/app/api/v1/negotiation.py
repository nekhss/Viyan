from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.negotiation import Negotiation
from app.schemas.negotiation import NegotiationCreate, NegotiationResponse


router = APIRouter(prefix="/negotiations", tags=["Negotiations"])


@router.post("/", response_model=NegotiationResponse)
def create_negotiation(negotiation: NegotiationCreate, db: Session = Depends(get_db)):
    new_negotiation = Negotiation(
        simulation_id=negotiation.simulation_id,
        status=negotiation.status,
        final_decision=negotiation.final_decision,
    )

    db.add(new_negotiation)
    db.commit()
    db.refresh(new_negotiation)

    return new_negotiation


@router.get("/", response_model=list[NegotiationResponse])
def get_negotiations(db: Session = Depends(get_db)):
    return db.query(Negotiation).all()
