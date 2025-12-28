from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.services.excel_importer import import_excel

router = APIRouter()

@router.post("/import")
def import_shifts(file: UploadFile, db: Session = Depends(get_db)):
    path = f"data/uploads/{file.filename}"
    with open(path, "wb") as f:
        f.write(file.file.read())

    import_excel(path, db)
    return {"status": "imported"}

