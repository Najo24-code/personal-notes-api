from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from auth import User

class Nota(Base):
    __tablename__ = 'notas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey('users.id'))
    usuario = relationship(User, backref='notas')