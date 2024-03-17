#!/usr/bin/python3
"""
This script accepts an input parameter and
outputs all entries from the 'states' table
where the 'name' column matches the input
in the 'hbtn_0e_0_usa' database.
It is designed to be secure against
SQL injection attacks.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Connect to the database and retrieve the
    list of states from it.
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
