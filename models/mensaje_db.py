from database.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

class MensajeDB(Base):
    __tablename__ = "mensajes"
    
    id = Column(Integer, primary_key=True, index=True)
    conversacion_id = Column(Integer, ForeignKey("conversaciones.id"), nullable=False)
    rol =  Column(String(20),nullable=False)
    contenido = Column(Text, nullable=False)
    fecha_envio = Column(DateTime, default=datetime.now)
    
    conversacion = relationship("ConversacionDB", back_populates="mensajes")