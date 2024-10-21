import sqlite3

con = sqlite3.connect("example.db")  # create a connection to the database
con.close()  # close the connection
