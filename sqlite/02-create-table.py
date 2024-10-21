import sqlite3

con = sqlite3.connect("sqlite/example.db")  # create a connection to the database
cursos = con.cursor()  # create a cursor object

# create a table
cursos.execute(
    """
  CREATE TABLE if not exists usuarios
  (id INTEGER PRIMARY KEY, nombre VARCHAR(100);
  """
)

con.commit()  # commit the changes
con.close()  # close the connection
