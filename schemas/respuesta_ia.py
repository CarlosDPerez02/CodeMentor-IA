from pydantic import BaseModel,ConfigDict

class RespuestaIA(BaseModel):
    respuesta: str
    model_config = ConfigDict(from_attributes=True) 