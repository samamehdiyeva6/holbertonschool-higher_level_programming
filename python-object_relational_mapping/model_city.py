#!/usr/bin/python3
"sdfsdfs"


import MySQLdb
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base

engine = create_engine("sqlite:///cities.db")

Base.metadata.create_all(engine)


class City(Base):
    "jdsfgdf"
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")


Session = sessionmaker(engine)
session = Session()
