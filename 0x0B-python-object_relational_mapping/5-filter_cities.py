#!/usr/bin/python3
"""Script that lists all cities of a state from the database hbtn_0e_4_usa"""

import sys
import MySQLdb


def filter_cities():
    """Function that filters cities from database"""
    # Take arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name)

    # Create cursor to execute queries
    cur = conn.cursor()

    # Execute query
    cur.execute("SELECT cities.name FROM cities JOIN states \
                ON cities.state_id = states.id WHERE states.name = %s \
                ORDER BY cities.id ASC", (state_name,))

    # Fetch results
    rows = cur.fetchall()

    # Print results
    if len(rows) == 0:
        print("")
    else:
        cities = [row[0] for row in rows]
        print(", ".join(cities))

    # Close cursor and database connection
    cur.close()
    conn.close()


if __name__ == '__main__':
    filter_cities()
