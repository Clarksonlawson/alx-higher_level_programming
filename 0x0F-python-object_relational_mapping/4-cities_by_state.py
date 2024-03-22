#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def cities_by_state(username, password, database):
    """Connect to the database and retrieve all cities sorted by state."""
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database, charset="utf8")
        # Create a cursor object
        cursor = db.cursor()
        # Prepare SQL query
        query = """SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id ASC"""
        # Execute SQL query
        cursor.execute(query)
        cities = cursor.fetchall()
        # Display results
        for city in cities:
            print(city)
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

    # Call the cities_by_state function
    cities_by_state(username, password, database)
