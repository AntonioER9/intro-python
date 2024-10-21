import sqlite3

with sqlite3.connect("sqlite/example.db") as con:
    cursos = con.cursor()  # create a cursor object

    # create a table
    cursos.execute(
        """
    CREATE TABLE if not exists usuarios
    (id INTEGER PRIMARY KEY, nombre VARCHAR(100);
    """
    )
