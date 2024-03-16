#!/usr/bin/python3
import MySQLdb
import sys

def get_cities_by_state(username, password, db_name):
        """Retrieve and display all cities from the database."""
            try:
                        # Connect to MySQL server
                                db = MySQLdb.connect(
                                                    host="localhost",
                                                                port=3306,
                                                                            user=username,
                                                                                        passwd=password,
                                                                                                    db=db_name
                                                                                                            )
                                        cursor = db.cursor()
                                                
                                                        # Execute query to retrieve cities with corresponding state names
                                                                cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id")
                                                                        
                                                                                # Fetch all rows
                                                                                        rows = cursor.fetchall()
                                                                                                
                                                                                                        # Display results
                                                                                                                for row in rows:
                                                                                                                                print(row)
                                                                                                                                        
                                                                                                                                                # Close cursor and database connection
                                                                                                                                                        cursor.close()
                                                                                                                                                                db.close()
                                                                                                                                                                    except MySQLdb.Error as e:
                                                                                                                                                                                print("MySQL Error:", e)
                                                                                                                                                                                        sys.exit(1)

                                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                # Check if correct number of arguments provided                 
                                                                                                                                                                                                    if len(sys.argv) != 4:
                                                                                                                                                                                                                print("Usage: {} username password database".format(sys.argv[0]))
                                                                                                                                                                                                                        sys.exit(1)
                                                                                                                                                                                                                            
                                                                                                                                                                                                                                # Get arguments from command line
                                                                                                                                                                                                                                    username, password, db_name = sys.argv[1:]
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                            # Call the function to get cities by state
                                                                                                                                                                                                                                                get_cities_by_state(username, password, db_name)

