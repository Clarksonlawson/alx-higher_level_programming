#!/usr/bin/python3

import sys
import MySQLdb

def select_states(username, password, database):
    """Select and display all states from the given database."""
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database, charset="utf8")
        # Create a cursor object
        cursor = db.cursor()
        # Execute SQL query to select all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        # Display results
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the select_states function
    select_states(username, password, database)

