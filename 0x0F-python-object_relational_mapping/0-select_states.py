#!/usr/bin/python3
"""Lists all states from the hbtn_0e_0_usa database"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(users=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM `states`")
    states = curs.fetchall()

    for state in states:
        print(state)
