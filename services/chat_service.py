from fastapi import HTTPException
from models.conversacion_db import ConversacionDB
from models.mensaje_db import MensajeDB
from core.config import cliente_groq
from core.prompts import PROMPT_IA
from schemas.respuesta_ia import RespuestaIA

def crear_respuesta(respuesta: str) -> RespuestaIA:
    return RespuestaIA(respuesta=respuesta)

def crear_conversacion(db):
    conversacion = ConversacionDB()
    db.add(conversacion)
    db.commit()
    db.refresh(conversacion)
    
    return conversacion
    

def guardar_mensaje(db,conversacion_id,rol,contenido):
    mensaje = MensajeDB(
        conversacion_id = conversacion_id,
        rol = rol,
        contenido =  contenido
    )
    
    db.add(mensaje)
    db.commit()
    db.refresh(mensaje)
    
    return mensaje
    
async def consultar_groq(pregunta: str):
    try:
        respuesta = await cliente_groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
        {
        "role": "system",
        "content": PROMPT_IA
        },
        {
        "role": "user",
        "content": pregunta
        }
    ],
    temperature=0.3,
        )
        return respuesta.choices[0].message.content
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error:{str(e)}")
        

async def procesar_chat(db, pregunta:str, conversacion_id: int | None = None):
    
    if conversacion_id is None:
        conversacion = crear_conversacion(db)
        conversacion_id = conversacion.id
    
    guardar_mensaje(
        db,
        conversacion_id,
        "user",
        pregunta
        )
    
    respuesta = await consultar_groq(pregunta)
    
    guardar_mensaje(
        db,
        conversacion.id,
        "assistant",
        respuesta
        )
    
    return crear_respuesta(respuesta)
    