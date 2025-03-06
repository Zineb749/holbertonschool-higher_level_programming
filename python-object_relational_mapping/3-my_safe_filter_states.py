#!/usr/bin/python3

""" script that list all states matching with script, SQL Injection"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    cursor.close()
    db.close()
