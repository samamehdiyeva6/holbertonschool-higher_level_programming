#!/usr/bin/python3
"""Lists all State objects from a MySQL database"""

import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State, City).join(City, City.state_id == State.id).order_by(City.id).all()
    for state in states:
        print(f"{state.name}: ({City.id}) {City.name}")

    session.commit()
    session.close()
