#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
import sys


if __name__ == '__main__':
    # Database connection
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    # Cursor class
    cur = conn.cursor()

    # Query
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    # Results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()
