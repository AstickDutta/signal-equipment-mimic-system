from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api.api import api_router
from app.config.database import engine, Base

# Load environment variables from .env file
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Signal Equipment API",
    description="A FastAPI backend for managing signal equipment with CI/CD pipeline",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to Signal Equipment API",
        "status": "running",
        "version": "1.0.0",
        "ci_cd": "enabled",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "signal-equipment-api"}