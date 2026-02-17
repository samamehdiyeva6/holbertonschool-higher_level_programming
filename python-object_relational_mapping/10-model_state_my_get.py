#!/usr/bin/python3
"""Lists all State objects from a MySQL database"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

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

    states = session.query(State).order_by(State.id).all()
    count = 0
    for state in states:
        if state.name == sys.argv[4]:
            print(state.id)
            count += 1
            break
    if count == 0:
        print("Not found")

    session.close()
