from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import shifts, swaps, admin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Guard Shift Swap")

app.include_router(shifts.router, prefix="/shifts")
app.include_router(swaps.router, prefix="/swaps")
app.include_router(admin.router, prefix="/admin")

