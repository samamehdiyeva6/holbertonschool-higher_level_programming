#!/usr/bin/python3
"dsfsdfsd"

from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    username = sys.argv[1]
    password =  sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping = True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
