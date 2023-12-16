"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    userName = Column(String(60), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    fullName = Column(String(60), nullable=False)
    isBlocked = Column(Boolean, nullable=False, default=False)
    role = Column(String(60), nullable=False)
    secretKey = Column(String(60), nullable=False, unique=True)
