"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Revenue(BaseModel, Base):
    """This class defines a revenue"""

    __tablename__ = "revenues"
    name = Column(String(60), nullable=False)
