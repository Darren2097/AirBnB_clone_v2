#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """ State class """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """
            """

            city_dict = models.storage.all('City')
            city_list = []
            for city in city_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
