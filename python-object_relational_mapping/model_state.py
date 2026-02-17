#!/usr/bin/python3
"vsdfsdfds"

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine("sqlite:///states.db")

Base.metadata.create_all(engine)


class State(Base):
    "sdfsdfsd"
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")


Session = sessionmaker(bind=engine)
session = Session()
