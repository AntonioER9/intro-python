import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursos = con.cursor()  # create a cursor object

    cursos.execute(
        "insert into usuarios values(?,?)",
        (1, "Juan"),
    )
