#!/usr/bin/python3
"""a script that lists all states with a
name starting with N (upper N) from the database
hbtn_0e_0_usa:"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    DB_Name = sys.argv[3]

    DB = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=DB_Name,
                         charset="utf8")
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM states WHERE name like 'N%'")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    DB.close()