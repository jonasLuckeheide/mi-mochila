from fastapi import APIRouter
from app.api.v1.endpoints import planificaciones

api_router = APIRouter()
api_router.include_router(planificaciones.router, prefix="/planificaciones", tags=["planificaciones"])
