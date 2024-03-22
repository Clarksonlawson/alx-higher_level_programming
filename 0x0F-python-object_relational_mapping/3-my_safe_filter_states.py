#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from MySQL injections.
"""
import sys
import MySQLdb


def safe_filter_states(username, password, database, state_name):
    """Filter and display states where name matches the provided argument."""
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database, charset="utf8")
        # Create a cursor object
        cursor = db.cursor()
        # Prepare SQL query using parameterized query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        # Execute SQL query with state_name as parameter
        cursor.execute(query, (state_name,))
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
    if len(sys.argv) != 5:
        print(
            "Usage: {} username password database state_name".format(
                sys.argv[0]))
        sys.exit(1)

    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the safe_filter_states function
    safe_filter_states(username, password, database, state_name)
