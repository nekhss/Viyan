from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.mission import router as mission_router
from app.api.v1.satellite import router as satellite_router
from app.api.v1.simulation import router as simulation_router
from app.api.v1.negotiation import router as negotiation_router
from app.api.v1.mcp import router as mcp_router

api_router = APIRouter(prefix="/api/v1")


api_router.include_router(health_router)
api_router.include_router(mission_router)
api_router.include_router(satellite_router)
api_router.include_router(simulation_router)
api_router.include_router(negotiation_router)
api_router.include_router(mcp_router)
