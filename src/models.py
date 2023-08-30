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
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
