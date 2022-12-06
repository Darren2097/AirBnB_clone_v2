#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for name, value in kwargs.items():
                if name != '__class__':
                    if name == 'created_at' or name == 'updated_at':
                        value = datetime(strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    setattr(self, name, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
                setattr(self, 'created_at', datetime.utcnow())
                self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""

        cpdict = dict(self.__dict__)
        cpdict['__class__'] = type(self).__name__
        cpdict['created_at'] = cpdict['created_at'].isoformat()
        cpdict['updated_at'] = cpdict['updated_at'].isoformat()
        cpdict.pop('_sa_instance_state', None)
        return cpdict

    def delete(self):
        """deletes the current instance from the storage"""

        models.storage.delete(self)
