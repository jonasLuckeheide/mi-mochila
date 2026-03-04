from typing import Optional
from datetime import datetime
from app.models.planificacion import PlanificacionBase

class PlanificacionCreate(PlanificacionBase):
    pass

class PlanificacionRead(PlanificacionBase):
    id: int
    created_at: datetime

class PlanificacionUpdate(PlanificacionBase):
    nombre: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    tipo_planificacion: Optional[str] = None
    campo_experiencia: Optional[str] = None
    edad_desde: Optional[int] = None
    edad_hasta: Optional[int] = None

