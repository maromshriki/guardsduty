from sqlalchemy import Column, Integer, Boolean, ForeignKey
from app.core.database import Base

class SwapMatch(Base):
    __tablename__ = "swap_matches"

    id = Column(Integer, primary_key=True)
    shift_a_id = Column(Integer, ForeignKey("shifts.id"))
    shift_b_id = Column(Integer, ForeignKey("shifts.id"))

    approved_a = Column(Boolean, default=False)
    approved_b = Column(Boolean, default=False)

