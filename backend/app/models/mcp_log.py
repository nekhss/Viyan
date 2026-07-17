from sqlalchemy import Column, Integer, String, Text

from app.database.database import Base


class MCPLog(Base):
    __tablename__ = "mcp_logs"

    id = Column(Integer, primary_key=True, index=True)
    tool = Column(String, nullable=False)
    request = Column(Text)
    response = Column(Text)
    status = Column(String, default="SUCCESS")
