from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Nota
from schemas import NotaBase, NotaCreate, NotaResponse
from auth import User, get_current_user

router = APIRouter()

@router.get("/notas/", response_model=list[NotaResponse])
def read_notas(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    notas = db.query(Nota).filter(Nota.usuario_id == current_user.id).all()
    return notas

@router.get("/notas/{nota_id}", response_model=NotaResponse)
def read_nota(nota_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    nota = db.query(Nota).filter(Nota.id == nota_id).filter(Nota.usuario_id == current_user.id).first()
    if nota is None:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return nota

@router.post("/notas/", response_model=NotaResponse)
def create_nota(nota: NotaCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    nota_db = Nota(titulo=nota.titulo, contenido=nota.contenido, usuario_id=current_user.id)
    db.add(nota_db)
    db.commit()
    db.refresh(nota_db)
    return nota_db

@router.delete("/notas/{nota_id}")
def delete_nota(nota_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    nota = db.query(Nota).filter(Nota.id == nota_id).filter(Nota.usuario_id == current_user.id).first()
    if nota is None:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    db.delete(nota)
    db.commit()
    return {"mensaje": "Nota eliminada con éxito"}