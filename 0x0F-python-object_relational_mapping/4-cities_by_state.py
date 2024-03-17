#!/usr/bin/env python3
"""
This script lists all cities from the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv


def main():
    """
    Access the database and retrieve the cities from the database.
    """
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=argv[1], passwd=argv[2], db=argv[3])
    with db_connection.cursor() as cursor:
        cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """)
        rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()
