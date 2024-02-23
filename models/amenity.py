#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import environ
# from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ A amenity classe that describe amenities of all places or people"""

    __tablename__ = "amenities"

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
    else:
        name = ""
