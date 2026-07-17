from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.simulation import router as simulation_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(simulation_router)