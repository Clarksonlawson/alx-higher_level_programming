nges the name of a State object from the database hbtn_0e_6_usa"""

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
                                                                            
                                                                                # Query the state with id = 2
                                                                                    state_to_update = session.query(State).filter_by(id=2).first()
                                                                                        
                                                                                            # Change the name of the state
                                                                                                if state_to_update:
                                                                                                        state_to_update.name = "New Mexico"
                                                                                                                
                                                                                                                        # Commit the session to persist the changes
                                                                                                                                session.commit()
                                                                                                                                    
                                                                                                                                        # Close the session
                                                                                                                                            session.close()
