from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class Negotiation(Base):
    __tablename__ = "negotiations"

    id = Column(Integer, primary_key=True, index=True)
    simulation_id = Column(Integer, ForeignKey("simulation_sessions.id"))
    status = Column(String, default="ONGOING")
    final_decision = Column(String)
