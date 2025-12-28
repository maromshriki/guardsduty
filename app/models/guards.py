from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Guard(Base):
    __tablename__ = "guards"

    id = Column(Integer, primary_key=True)
    name_original = Column(String, nullable=False)
    name_normalized = Column(String, unique=True, nullable=False)

