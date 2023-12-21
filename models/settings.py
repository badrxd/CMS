"""This module defines a class Settings"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean


class Settings(BaseModel, Base):
    """This class defines a app Settings"""

    __tablename__ = 'settings'
    company_name = Column(String(60), nullable=False,
                          default='Car Rent System Management')
    path_logo = Column(String(255), nullable=False)
    currency = Column(String(10), nullable=False)
    images_path = Column(String(255), nullable=False,
                         default='D:\\crms\\images')
    developers = Column(String(255), nullable=False)
    is_dark = Column(Boolean, nullable=False, default=False)
    backup_path = Column(String(255), nullable=False,
                         default='D:\\crms\\backups')
    report_path = Column(String(255), nullable=False,
                         default='D:\\crms\\reports')
    language = Column(String(20), nullable=False, default='en')
