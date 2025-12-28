from sqlalchemy import Column, Integer, Date, Time, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)

    guard_id = Column(Integer, ForeignKey("guards.id"), nullable=False)
    position_id = Column(Integer, ForeignKey("positions.id"), nullable=False)

    guard = relationship("Guard")
    position = relationship("Position")

    __table_args__ = (
        UniqueConstraint("date", "start_time", "position_id", name="uq_shift"),
    )

