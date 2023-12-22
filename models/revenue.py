"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Revenue(BaseModel, Base):
    """This class defines a revenue"""

    __tablename__ = 'revenues'
    time = Column(String(60), nullable=False)
    month = Column(String(60), nullable=False)
    year = Column(String(60), nullable=False)
    amount = Column(Integer, nullable=False, default=0)
    resetvations = relationship('Reservation', backref='revenue')
