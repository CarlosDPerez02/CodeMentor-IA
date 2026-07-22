from database.db import Base
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

class ConversacionDB(Base):
    __tablename__ = "conversaciones"
    
    id = Column(Integer, primary_key=True, index=True)
    fecha_inicio = Column(DateTime, default=datetime.now)
    
    mensajes = relationship("MensajeDB", back_populates="conversacion")