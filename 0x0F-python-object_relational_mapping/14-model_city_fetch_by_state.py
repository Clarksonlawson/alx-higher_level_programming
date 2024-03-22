#!/usr/bin/python3
"""Print all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

        # Query the cities and their respective states
        cities = session.query(City, State).join(State).order_by(City.id).all()

        # Print the results
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

            # Close the session
            session.close()
