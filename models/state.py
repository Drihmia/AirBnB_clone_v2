#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
    @property
    def cities(self):
        from models.city import City
        from models import storage

        list_cities_state_id = []
        for city in storage.all(City):
            if (city.state_id == self.id):
                list_cities_state_id.append(city)

        return list_cities_state_id
