#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    # Execute the SQL query to select the first 5 states and order by ID
    cur.execute("SELECT * FROM states ORDER BY states.id LIMIT 5")

    # Fetch all the rows and print them
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i])

    # Close the cursor and connection
    cur.close()
    db.close()
