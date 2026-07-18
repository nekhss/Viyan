from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

from app.database.database import Base


class NegotiationStep(Base):
    __tablename__ = "negotiation_steps"

    id = Column(Integer, primary_key=True, index=True)
    negotiation_id = Column(Integer, ForeignKey("negotiations.id"))
    step = Column(Integer, nullable=False)
    proposer = Column(String, nullable=False)
    maneuver = Column(String, nullable=False)
    fuel_cost = Column(Float, nullable=False)
    accepted = Column(Boolean, default=False)
