#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa"""

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

        # Create new State object
        new_state = State(name="Louisiana")

        # Add the new state to the session
        session.add(new_state)

        # Commit the session to persist the changes
        session.commit()

        # Print the new states.id after creation
        print(new_state.id)

        # Close the session
        session.close()
