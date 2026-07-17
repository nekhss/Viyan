from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.mission import router as mission_router
from app.api.v1.satellite import router as satellite_router


api_router = APIRouter(prefix="/api/v1")


api_router.include_router(health_router)
api_router.include_router(mission_router)
api_router.include_router(satellite_router)
