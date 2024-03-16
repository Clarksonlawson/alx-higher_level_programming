#!/usr/bin/python3
import MySQLdb
import sys
def filter_states_by_name_starting_with_N(username, password, db_name):
        """Retrieve and display states with names starting with 'N'."""
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
                                                
                                                        # Execute query to retrieve states with names starting with 'N'
                                                                cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
                                                                        
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
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                            # Call the function to filter states by name starting with 'N'
                                                                                                                                                                                                                                                filter_states_by_name_starting_with_N(username, password, db_name)
