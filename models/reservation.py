"""This module defines a class Reservation"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime, Enum


# class Status(Enum):
#     confirmed = 'confirmed'
#     cancelled = 'cancelled'
#     pending = 'pending'


class Reservation(BaseModel, Base):
    """This class defines a reservation by various attributes"""

    __tablename__ = 'reservations'
    customer_id = Column(String(60), ForeignKey(
        'customers.id'), nullable=False)
    car_id = Column(String(60), ForeignKey('cars.id'), nullable=False)
    revenue_id = Column(String(60), ForeignKey('revenues.id'),  nullable=False)
    rev_number = Column(Integer, nullable=False, default=0)
    status = Column(Enum('confirmed', 'cancelled', 'pending', name='status_enum'),
                    nullable=False, default='confirmed', )
    # status = Column(Enum(Status), nullable=False, default=Status.pending)
    amount = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
