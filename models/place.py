#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import environ

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    amenity_ids = []

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """return a list of Review instances by place"""
            from models.review import Review
            from models import storage

            list_reviews_place_id = []
            for review in storage.all(Review).values():
                if (review.place_id == self.id):
                    list_reviews_place_id.append(review)

            return list_reviews_place_id

        @property
        def amenities(self):
            """returns a list of amenities by place (that their id stored in
            the classe attribute amenity_ids in this class
            """
            from models.amenity import Amenity
            from models import storage

            list_amenities_place_id = []
            for amenity in storage.all(Amenity).values():
                if (amenity.id in self.amenity_ids):
                    list_amenities_place_id.append(amenity)
            return list_amenities_place_id

        @amenities.setter
        def amenities(self, value):
            """setter that adds ids of all amenties to amenity_ids
            this methode accept only Amenity objects
            """
            from models.amenity import Amenity

            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
