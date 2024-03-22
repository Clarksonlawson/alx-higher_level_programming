#!/usr/bin/python3
import MySQLdb
import sys


def filter_cities_by_state(username, password, db_name, state_name):
    """Retrieve and display all cities of a given state."""
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

        # Create parameterized SQL query
        sql_query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"

        # Execute query with user input as parameter
        cursor.execute(sql_query, (state_name,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Extract city names from the rows
        cities = [row[0] for row in rows]

        # Display results
        if cities:
            print(", ".join(cities))
            else:
                print("No cities found for the state '{}'".format(state_name))

                # Close cursor and database connection
                cursor.close()
                db.close()
                except MySQLdb.Error as e:
                    print("MySQL Error:", e)
                    sys.exit(1)

                    if __name__ == "__main__":
                        # Check if correct number of arguments provided
                        if len(
                                sys.argv) != 5:
                            print(
                                "Usage: {} username password database state_name".format(
                                    sys.argv[0]))
                            sys.exit(1)

                            # Get arguments from command line
                            username, password, db_name, state_name = sys.argv[1:]

                            # Call the function to filter cities by state
                            filter_cities_by_state(
                                username, password, db_name, state_name)
