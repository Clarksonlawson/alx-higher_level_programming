#!/usr/bin/python3
import MySQLdb
import sys

def filter_states_by_name(username, password, db_name, state_name):
        """Retrieve and display states with names matching the input."""
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
                                                
                                                        # Create SQL query with user input
                                                                sql_query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
                                                                        
                                                                                # Execute query with user input as parameter
                                                                                        cursor.execute(sql_query, (state_name,))
                                                                                                
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
                                                                                                                                                                                                                            if len(sys.argv) != 5:
                                                                                                                                                                                                                                        print("Usage: {} username password database state_name".format(sys.argv[0]))
                                                                                                                                                                                                                                                sys.exit(1)
                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                        # Get arguments from command line
                                                                                                                                                                                                                                                            username, password, db_name, state_name = sys.argv[1:]
                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                    # Call the function to filter states by user input
                                                                                                                                                                                                                                                                        filter_states_by_name(username, password, db_name, state_name)

