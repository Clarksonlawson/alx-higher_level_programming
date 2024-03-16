#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
        # Check if correct number of arguments provided
            if len(sys.argv) != 5:
                        print("Usage: {} username password database state_name".format(sys.argv[0]))
                                sys.exit(1)
                                    
                                        # Get arguments from command line
                                            username, password, db_name, state_name = sys.argv[1:]

                                                # Connect to MySQL server
                                                    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
                                                        
                                                            # Create session factory bound to the engine
                                                                Session = sessionmaker(bind=engine)
                                                                    
                                                                        # Create a session
                                                                            session = Session()
                                                                                
                                                                                    # Query State object with the given state name
                                                                                        state = session.query(State).filter(State.name == state_name).first()
                                                                                            
                                                                                                # Check if state is found
                                                                                                    if state:
                                                                                                                print(state.id)
                                                                                                                    else:
                                                                                                                                print("Not found")

                                                                                                                                    # Close the session
                                                                                                                                        session.close()
                                                                                                                                        
