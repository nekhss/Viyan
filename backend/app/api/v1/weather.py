from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_weather():
    return {"message": "Weather API working"}
