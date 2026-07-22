from fastapi import APIRouter, Depends
from schemas.preguntas_create import PreguntasCreate
from schemas.respuesta_ia import RespuestaIA
from sqlalchemy.orm import Session
from database.dependency import get_db
from services.chat_service import procesar_chat

router = APIRouter(
    prefix="/preguntas",
    tags=["Preguntas"]
)

@router.post("/preguntas", response_model=RespuestaIA)
async def consultas(preguntas:PreguntasCreate, db: Session = Depends(get_db)):
    return await procesar_chat(db,preguntas.pregunta)