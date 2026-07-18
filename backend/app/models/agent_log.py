from sqlalchemy import Column, Integer, String, Text, ForeignKey

from app.database.database import Base


class AgentLog(Base):
    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True, index=True)
    simulation_id = Column(Integer, ForeignKey("simulation_sessions.id"))
    agent_name = Column(String, nullable=False)
    action = Column(String, nullable=False)
    message = Column(Text)
