#!/usr/bin/python3
"""This is the Amenity class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship

# Define the association table
association_table = Table(
    'place_amenities',
    Base.metadata,
    Column('place_id', Integer, ForeignKey('places.id')),
    Column('amenity_id', Integer, ForeignKey('amenities.id'))
)

class Amenity(BaseModel, Base):
    """This class defines amenities
    Attributes:
        name: name (string, 128 chars, not null)
        place_amenities: many-to-many relationship with place
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    # Define the many-to-many relationship with Place
    place_amenities = relationship('Place', secondary=association_table, back_populates='amenities')