from fastapi import APIRouter

from app.api.endpoints import signals_router, aspects_router

api_router = APIRouter()

api_router.include_router(signals_router, prefix="/signals", tags=["signals"])
api_router.include_router(aspects_router, prefix="/aspects", tags=["aspects"])
