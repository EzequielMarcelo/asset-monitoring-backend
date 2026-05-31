from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base

class Variable(Base):
    __tablename__ = "variables"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=True)
    value = Column(Float, nullable=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))