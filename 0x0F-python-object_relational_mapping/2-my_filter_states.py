#!/usr/bin/python3
"""a script that display all the values of state where name matches the argument from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name
                LIKE '{:s}' ORDER BY \id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

