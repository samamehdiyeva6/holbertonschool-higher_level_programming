#!/usr/bin/python3
import MySQLdb
conn = MySQLdb.connect(host="localhost", port=3306, user="sama'@'localhost", passwd="mypassword", db="hbtn_0e_0_usa")
cur = conn.cursor()
cur.execute("SELECT id, name FROM states ORDER BY states.id")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
