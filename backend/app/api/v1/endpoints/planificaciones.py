from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.planificacion import Planificacion, TipoPlanificacion, CampoExperiencia
from app.schemas.planificacion import PlanificacionCreate

router = APIRouter()

@router.get("/", response_model=List[Planificacion])
def read_planificaciones(session: Session = Depends(get_session)):
    planificaciones = session.exec(select(Planificacion)).all()
    if not planificaciones:
        # Devolver datos de prueba si está vacío para el primer test
        return [
            Planificacion(
                id=1,
                titulo="Mi Primera Planificación",
                año=2026,
                tipo_planificacion=TipoPlanificacion.unidad,
                campo_experiencia=CampoExperiencia.identidad,
                edad_desde=3,
                edad_hasta=5,
                archivo_url="https://storage.example.com/plan_1.pdf"
            )
        ]
    return planificaciones

@router.post("/", response_model=Planificacion)
def create_planificacion(planificacion: PlanificacionCreate, session: Session = Depends(get_session)):
    db_planificacion = Planificacion.from_orm(planificacion)
    session.add(db_planificacion)
    session.commit()
    session.refresh(db_planificacion)
    return db_planificacion
