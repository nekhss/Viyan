from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health():
    return {
        "status": "UP",
        "backend": "running",
        "database": "pending",
        "simulation": "pending",
        "mcp": "pending",
    }
