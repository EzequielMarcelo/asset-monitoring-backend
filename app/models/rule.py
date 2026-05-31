from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base

class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True)
    operator = Column(String, nullable=False)
    value = Column(Float, nullable=True)
    variable_id = Column(Integer, ForeignKey("variables.id"))   