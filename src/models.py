import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class Identity(Base):  
    __tablename__ = 'identity'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    descrption = Column(String(250))
    
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    mass = Column(String(250))
    heigth = Column(String(250))
    gender = Column(String(250))
    birth_year = Column(String(250))
    identity_id = Column(Integer, ForeignKey('identity.id'))
    identity = relationship(Identity)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String(250))
    diameter = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    terrain = Column(String(250))
    orbital_period = Column(String(250))
    rotation_period = Column(String(250))
    identity_id = Column(Integer, ForeignKey('identity.id'))
    identity = relationship(Identity)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    length = Column(String(250))
    passengers= Column(String(250))
    manufacturer = Column(String(250))
    vehicle_class = Column(String(250))
    cargo_capacity = Column(String(250))
    crew = Column(String(250))
    cost_in_credits = Column(String(250))
    identity_id = Column(Integer, ForeignKey('identity.id'))
    identity = relationship(Identity)



class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    identity_id = Column(Integer, ForeignKey('identity.id'))
    identity = relationship(Identity)

    
   

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
