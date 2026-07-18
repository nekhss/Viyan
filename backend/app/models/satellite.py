from sqlalchemy import Column, Integer, String, Float

from app.database.database import Base


class Satellite(Base):
    __tablename__ = "satellites"

    id = Column(Integer, primary_key=True, index=True)
    satellite_id = Column(String(50), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    fuel = Column(Float, nullable=False)
    priority = Column(String(20), nullable=False)
    mission = Column(String(100), nullable=False)
    tle = Column(String, nullable=False)
    status = Column(String(20), default="ACTIVE")
