from pydantic import BaseModel
from datetime import date, time

class ShiftOut(BaseModel):
    id: int
    date: date
    start_time: time
    guard_id: int
    position_id: int

    class Config:
        orm_mode = True

