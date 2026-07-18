from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class WeatherCache(Base):
    __tablename__ = "weather_cache"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False)
    source = Column(String, nullable=False)
    data = Column(Text, nullable=False)
