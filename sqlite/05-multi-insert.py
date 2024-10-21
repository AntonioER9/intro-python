import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursos = con.cursor()  # create a cursor object

    cursos.executemany(
        "insert into usuarios values(?,?)",
        (2, "Juancho"),
        (3, "Juanita"),
    )
