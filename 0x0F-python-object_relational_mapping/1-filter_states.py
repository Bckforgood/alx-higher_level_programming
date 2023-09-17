#!/usr/bin/python3
"""This script prints all the satetes from the database starting
+ only with 'N'"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cr = db.cursor()

    cr.execute(
            'SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id ASC'
    )
    [print(state) for state in cr.fetchall() if state[1][0] == "N"]
