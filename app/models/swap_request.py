from sqlalchemy import Column, Integer, ForeignKey, String
from app.core.database import Base

class SwapRequest(Base):
    __tablename__ = "swap_requests"

    id = Column(Integer, primary_key=True)
    shift_id = Column(Integer, ForeignKey("shifts.id"), nullable=False)
    status = Column(String, default="open")  # open / matched / done

