from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.swap import SwapCreate
from app.models.swap_request import SwapRequest
from app.services.swap_engine import try_match

router = APIRouter()

@router.post("/")
def create_swap(req: SwapCreate, db: Session = Depends(get_db)):
    swap = SwapRequest(shift_id=req.shift_id)
    db.add(swap)
    db.commit()
    db.refresh(swap)

    match = try_match(db, swap)
    return {"swap_id": swap.id, "matched": bool(match)}

