from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.shift import Shift

router = APIRouter()

@router.get("/")
def list_shifts(db: Session = Depends(get_db)):
    return db.query(Shift).all()

