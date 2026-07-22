from pydantic import BaseModel

class PreguntasCreate(BaseModel):
    conversacion_id: int | None = None
    pregunta: str