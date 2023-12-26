"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    userName = Column(String(60), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    fullName = Column(String(60), nullable=False)
    isBlocked = Column(Boolean, nullable=False, default=False)
    role = Column(Enum('admin', 'manager', 'employee', name='role_enum'),
                  nullable=False, )
    gender = Column(Enum('male', 'female', name='gender_enum'), nullable=False)
    secretKey = Column(String(60), nullable=False, unique=True)
