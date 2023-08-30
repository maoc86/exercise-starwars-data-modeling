import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users (Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Characters (Base): 
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Gender = Column(String(10), nullable=False)
    Height = Column(Integer, nullable=False)

class Planets (Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    moons = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)

class Weapons(Base):
    __tablename__ = "weapons"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    energy = Column(String(200), nullable=False)

class Fav_Char (Base):
    __tablename__ = "fav_char"
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)

class Fav_Planets (Base):
    __tablename__ = "fav_planets"
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)

class Fav_Weapons (Base):
    __tablename__ = "fav_weapons"
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    weapon_id = Column(Integer, ForeignKey('weapons.id'))
    weapon = relationship(Weapons)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
