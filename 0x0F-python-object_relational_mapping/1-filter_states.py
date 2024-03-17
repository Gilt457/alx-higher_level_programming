#!/usr/bin/env python3
"""
This script lists all states from the database hbtn_0e_0_usa
that start with the letter 'N'.
"""

import sys
import MySQLdb


def main():
    """Main entry point of the script."""
    db_connection = MySQLdb.connect(host='localhost',
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3],
                                    port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states "
                   "WHERE name LIKE BINARY 'N%' "
                   "ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    main()
