"""This module defines a class Car"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship


class Car(BaseModel, Base):
    """This class defines a car by various attributes"""

    __tablename__ = 'cars'
    brand = Column(String(60), nullable=False)
    image = Column(String(255), nullable=False)
    matricule = Column(String(60), nullable=False)
    rent_price = Column(Integer, nullable=False)
    availability = Column(Boolean, nullable=False, default=True)
    resirvations = relationship('Reservation', backref='car')
