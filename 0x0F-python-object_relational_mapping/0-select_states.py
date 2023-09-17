#!/usr/bin/python3
import MySQLdb
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        return

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password)
        cursor = db.cursor()

        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
        cursor.execute("USE {}".format(database_name))

        # Execute the query to retrieve states in ascending order by states.id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results in the specified format
        for result in results:
            print(result)

        # Close the cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error: Unable to connect to the database. {}".format(str(e)))

if __name__ == "__main__":
    main()
