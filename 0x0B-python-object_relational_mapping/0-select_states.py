#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa sorted in ascending order by id
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()
