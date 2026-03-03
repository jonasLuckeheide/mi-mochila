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
    titulo: str
    año: int
    tipo_planificacion: TipoPlanificacion
    campo_experiencia: CampoExperiencia
    edad_desde: int
    edad_hasta: int
    archivo_url: Optional[str] = None

class Planificacion(PlanificacionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
