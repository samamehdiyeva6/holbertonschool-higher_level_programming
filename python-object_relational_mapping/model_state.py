#!/usr/bin/python3
"vsdfsdfds"

from sqlalchemy import create_engine, Column, Integer, String, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///states.db")

Base.metadata.create_all(engine)

class State(Base):
    "sdfsdfsd"
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

Session = sessionmaker(bind = engine)
session = Session()
