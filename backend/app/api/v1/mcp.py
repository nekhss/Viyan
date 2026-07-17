from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.mcp_log import MCPLog
from app.schemas.mcp import MCPLogCreate, MCPLogResponse


router = APIRouter(prefix="/mcp", tags=["MCP"])


@router.post("/", response_model=MCPLogResponse)
def create_mcp_log(log: MCPLogCreate, db: Session = Depends(get_db)):
    new_log = MCPLog(
        tool=log.tool, request=log.request, response=log.response, status=log.status
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log


@router.get("/", response_model=list[MCPLogResponse])
def get_mcp_logs(db: Session = Depends(get_db)):
    return db.query(MCPLog).all()
