import sqlite3


def insert_db(db_name):
	connection=sqlite3.connect(db_name)
	ingress=input("Ingrese la tabla:")
	con=connection.cursor()
	con.execute("create table "+ingress+"(id integrer PRIMARY KEY)")
	
	connection.commit()
	print("Se ingreso la tabla " +ingress+ " a la Base de datos")