#!/usr/bin/python3
"""
This script takes an argument and displays all values in the states
where 'name' matches the argument from the database 'hbtn_0e_0_usa'.
This time, the script is safe from MySQL injections!
"""

import MySQLdb
from sys import argv


def fetch_states(user, password, db_name, state_name):
    """
    Connect to the database and fetch states where 'name' matches the argument.
    """
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=user, passwd=password, db=db_name)
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()
    cursor.close()
    connection.close()
    return states


if __name__ == "__main__":
    user_input = argv[1:5]
    states = fetch_states(*user_input)
    for state in states:
        print(state)
