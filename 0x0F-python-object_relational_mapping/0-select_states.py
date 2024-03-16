#!/usr/bin/python3
import MySQLdb
import sys

def get_states(username, password, db_name):
        """Retrieve and display all states from the database."""
            # Connect to MySQL server
                try:    
                            db = MySQLdb.connect(
                                                host="localhost",
                                                            port=3306,
                                                                        user=username,
                                                                                    passwd=password,
                                                                                                db=db_name
                                                                                                        )
                                    cursor = db.cursor()
                                            # Execute the query to retrieve states
                                                    cursor.execute("SELECT * FROM states ORDER BY id")
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
                                                                                                                                                                                                # Call the function to get states
                                                                                                                                                                                                    get_states(username, password, db_name)

