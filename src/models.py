import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    name_user = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email_user = Column(String(250), nullable=False)
    birth_user = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_planets = Column(Integer, primary_key=True)
    planets_name = Column(String(250), nullable=False)
    planets_diameter = Column(Integer, nullable=False)
    planets_rotation_period = Column(Integer, nullable=False)
    planets_orbital_period = Column(Integer, nullable=False)
    planets_gravity = Column(String(250), nullable=False)
    planets_population = Column(Integer, nullable=False)
    planets_climate = Column(String(250), nullable=False)
    planets_terrain = Column(String(250), nullable=False)
    planets_surface_water = Column(Integer, nullable=False)
    planets_created = Column(String(250), nullable=False)
    planets_edited = Column(String(250), nullable=False)
    planets_url = Column(String(250), nullable=False)
   
class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_people = Column(Integer, primary_key=True)
    people_height = Column(Integer, nullable=False)
    people_mass = Column(Integer, nullable=False)
    people_hair_color = Column(String(250), nullable=False)
    people_skin_color = Column(String(250), nullable=False)
    people_eye_color = Column(String(250), nullable=False)
    people_birth_year = Column(String(250), nullable=False)
    people_gender = Column(String(250), nullable=False)
    people_created = Column(String(250), nullable=False)
    people_edited = Column(String(250), nullable=False)
    people_name = Column(String(250), nullable=False)
    people_homeworld = Column(String(250), nullable=False)
    people_url = Column(String(250), nullable=False)
    planets_id_fk = Column(Integer, ForeignKey('planets.id_planets'))
    planets = relationship(Planets)

class Favorite(Base): 
    __tablename__ = 'favorite'
    id_favorite = Column(Integer, primary_key=True)
    user_id_fk = Column(Integer, ForeignKey('user.id_user'))
    user = relationship(User)
    planets_id_fk = Column(Integer, ForeignKey('planets.id_planets'))
    planets = relationship(Planets)
    people_id_fk = Column(Integer, ForeignKey('people.id_people'))
    people = relationship(People)
    type_favorite = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')