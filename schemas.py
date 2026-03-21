from pydantic import BaseModel
from typing import Optional
from auth import UserResponse

class NotaBase(BaseModel):
    titulo: str
    contenido: str

class NotaCreate(NotaBase):
    pass

class NotaResponse(NotaBase):
    id: int
    usuario: UserResponse

    class Config:
        from_attributes = True