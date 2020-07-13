import sqlite3

def create_db(db_name):
	connection = sqlite3.connect(db_name + ".db")
	connection.close()
	print (db_name + " Database is created!")

