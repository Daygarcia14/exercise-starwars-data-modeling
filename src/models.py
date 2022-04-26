import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key = True)
    favorite = relationship("favorite")
    email = Column(String(50), nullable = False, unique = True)
    password = Column(String(8), nullable = False, unique = True)
    loginstatus = Column(Boolean, nullable = False, unique = False, default = False)

class Favorite(Base):
    __tablename__= "favorite"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("user", backref = "favorite")
    planet = relationship("planet")
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character = relationship("character")
    character_id = Column(Integer, ForeignKey("character.id"))
    vehicle = relationship("vehicle")
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))

class Planet(Base):
    __tablename__= "planet"
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False, unique = True)
    population = Column(Integer, nullable = False)
    climate = Column(String(50), nullable = False)
    terrain = Column(String(50), nullable = False)
    diameter = Column(Integer, nullable = False)

class Character(Base):
    __tablename__= "character"
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False, unique = True)
    gender = Column(String(10), nullable = False)
    hair_color = Column(String(50), nullable = False)
    eye_color = Column(String(50), nullable = False)
    birth_year = Column(Date, nullable = False)

class Vehicle(Base):
    __tablename__= "vehicle"
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False, unique = True)
    model = Column(String(50), nullable = False)
    crew = Column(Float, nullable = False)
    passenger = Column(Float, nullable = False)
    length = Column(Integer, nullable = False)
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')