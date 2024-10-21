import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()  # create a cursor object
    cursor.execute("select * from usuarios where id = ?", (1,))
    print(cursor.fetchall())  # fetch all rows
