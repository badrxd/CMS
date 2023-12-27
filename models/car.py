"""This module defines a class Car"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship
# from models.reservation import Reservation


class Car(BaseModel, Base):
    """This class defines a car by various attributes"""

    __tablename__ = 'cars'
    brand = Column(String(60), nullable=False)
    car_image = Column(String(255), nullable=False)
    matricule = Column(String(60), nullable=False)
    rent_price = Column(Integer, nullable=False)
    currency = Column(String(10), nullable=False, default="DH")
    availability = Column(Boolean, nullable=False, default=True)
    reservations = relationship('Reservation', backref='car')
