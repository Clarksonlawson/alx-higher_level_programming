#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows using fetchall() method
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()
