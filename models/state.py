#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
        name = Column(String(128), nullable=False)
    else:
        name = ""

        @property
        def cities(self):
            """
            returns the list of City instances with state_id
            equals to the current State.id
            """
            from models.city import City
            from models import storage

            list_cities_state_id = []
            for city in storage.all(City).values():
                if (city.state_id == self.id):
                    list_cities_state_id.append(city)

            return list_cities_state_id
