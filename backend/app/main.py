from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router

app = FastAPI(
    title="Viyan Backend",
    version="1.0.0",
    description="Backend API for the Viyan Hackathon Project",
)

origins = [
    "http://localhost:5173",  # Vite frontend
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "Viyan Backend is running", "status": "OK"}
