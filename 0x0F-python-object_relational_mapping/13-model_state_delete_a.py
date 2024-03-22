 all State objects with a name containing the letter a"""

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
                                             engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
                                                 
                                                     # Create session factory bound to the engine
                                                         Session = sessionmaker(bind=engine)
                                                             
                                                                 # Create a session
                                                                     session = Session()
                                                                         
                                                                             # Query the states containing the letter 'a' in their name
                                                                                 states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
                                                                                     
                                                                                         # Delete the states
                                                                                             for state in states_to_delete:
                                                                                                     session.delete(state)
                                                                                                         
                                                                                                             # Commit the session to persist the changes
                                                                                                                 session.commit()
                                                                                                                     
                                                                                                                         # Close the session
                                                                                                                             session.close()
