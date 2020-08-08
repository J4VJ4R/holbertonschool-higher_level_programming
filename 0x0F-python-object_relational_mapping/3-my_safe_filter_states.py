#!/usr/bin/python3
"""a script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    DB_Name = sys.argv[3]
    search_state = sys.argv[4]

    DB = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=DB_Name,
                         charset="utf8")
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (search_state,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
