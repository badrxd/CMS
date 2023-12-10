"""This module defines a base class for all models in our project"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel():
    """A base class for all models"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if (k == "created_at" or k == "updated_at"):
                    continue
                else:
                    if k != '__class__':
                        self.__dict__[k] = v

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        safe_dict = self.__dict__.copy()
        if "created_at" in safe_dict:
            safe_dict["created_at"] = safe_dict["created_at"].strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in safe_dict:
            safe_dict["updated_at"] = safe_dict["updated_at"].strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        # safe_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in safe_dict:
            del safe_dict["_sa_instance_state"]
        return safe_dict

    def delete(self):
        """ Deletes instance"""
        models.storage.delete(self)
