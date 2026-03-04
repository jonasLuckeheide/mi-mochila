from datetime import datetime
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field

class TipoPlanificacion(str, Enum):
    unidad = "Unidad Didáctica"
    secuencia = "Secuencia Didáctica"
    proyecto = "Proyecto"

class CampoExperiencia(str, Enum):
    identidad = "Formación de identidad personal y social"
    comunicacion = "Comunicación y expresión"
    vida_cotidiana = "Vida cotidiana"

class PlanificacionBase(SQLModel):
    nombre: str
    descripcion: Optional[str] = None
    objetivos: Optional[str] = None
    contenidos: Optional[str] = None
    fecha_inicio: datetime
    fecha_fin: datetime
    tipo_planificacion: TipoPlanificacion
    campo_experiencia: CampoExperiencia
    edad_desde: int
    edad_hasta: int
    archivo_url: Optional[str] = None

class Planificacion(PlanificacionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
