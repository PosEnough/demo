import sqlite3 as sql

connect = sql.connect('storedatabase.db' )

cur = connect.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS store (Item TEXT, Qauntity INTEGER, Price REAL)")

cur.execute("INSERT INTO store VALUES('wine Glass',2,310.25)")

connect.commit()
connect.close()


