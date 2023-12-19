"""This module defines a class Customer"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship
from models.reservation import Reservation


class Customer(BaseModel, Base):
    """This class defines a customer by various attributes"""

    __tablename__ = 'customers'
    full_name = Column(String(60), nullable=False)
    phone = Column(String(60), nullable=False)
    card_id = Column(String(60))
    driver_id = Column(String(60))
    card_id_image = Column(String(255))
    driver_id_image = Column(String(255))
    blacklist = Column(Boolean, nullable=False, default=False)
    num_of_res = Column(Integer, nullable=False, default=0)
    spending = Column(Integer, nullable=False, default=0)
    reservations = relationship('Reservation', backref='customer')
