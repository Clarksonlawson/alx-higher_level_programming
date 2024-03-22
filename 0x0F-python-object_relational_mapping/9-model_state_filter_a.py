#!/usr/bin/python3
"""Lists all State objects that contain the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

        # Get arguments from command line
        username, password, db_name = sys.argv[1:]

        # Connect to MySQL server
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))

        # Create session factory bound to the engine
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query State objects containing the letter 'a' and print the results
        states_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(
            State.id).all()
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))

            # Close the session
            session.close()
