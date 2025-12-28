from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

