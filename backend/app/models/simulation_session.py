from sqlalchemy import Column, Integer, String, Float

from app.database.database import Base


class SimulationSession(Base):
    __tablename__ = "simulation_sessions"

    id = Column(Integer, primary_key=True, index=True)
    simulation_id = Column(String, unique=True, nullable=False)
    collision_probability = Column(Float, nullable=False)
    risk_prediction = Column(Float)
    confidence = Column(Float)
    status = Column(String, default="PENDING")
