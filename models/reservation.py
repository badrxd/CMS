"""This module defines a class Reservation"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime


class Reservation(BaseModel, Base):
    """This class defines a reservation by various attributes"""

    __tablename__ = 'reservations'
    customer_id = Column(String(60), ForeignKey('customers.id'), nullable=False)
    car_id = Column(String(60), ForeignKey('cars.id'), nullable=False)
    confirmed = Column(Boolean, nullable=False)
    amount = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
