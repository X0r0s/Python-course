import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
#from Funciones_Graficas.consulta_prod import consultaproductos


class creaalmacen(QDialog):
	def __init__(self):
		super().__init__()
		self.conex=sqlite3.connect("ALMACEN.db")
		self.c=self.conex.cursor()
		self.c.execute(""" CREATE TABLE IF NOT EXISTS PRODUCTOS(
    		ID_ST INTEGER PRIMARY KEY AUTOINCREMENT,
        	AT_ST VARCHAR(20) NOT NULL,
        	DT_ST VARCHAR(100) NOT NULL,
        	PS_ST REAL NOT NULL,
        	CN_ST INTEGER NOT NULL,
        	VL_ST REAL NOT NULL) """)
		self.inserta_producto_inicial()
		
		uic.loadUi("Formularios/consulta_productos.ui", self)
		self.pb_Consulta.clicked.connect(self.consulta_productos)
		

	def inserta_producto_inicial(self):
		borra="DELETE FROM PRODUCTOS"
		insertar = """INSERT INTO PRODUCTOS (ID_ST, AT_ST, DT_ST, PS_ST, CN_ST, VL_ST) VALUES
    	(NULL,"café","Exprés",0.25,0,0),(NULL,"café","Capuchino",0.5,0,0),
    	(NULL,"café","Moka",1,0,0),(NULL,"café","Filtrado",2,0,0),
		(NULL,"yerba","Elaborada con palo",0.25,0,0),(NULL,"yerba","Elaborada sin palo",0.5,0,0),
    	(NULL,"yerba","Caaminí",1,0,0),(NULL,"yerba","Testada",2,0,0),
		(NULL,"arroz","Blanco",0.25,0,0),(NULL,"arroz","Amarillo",0.5,0,0),
    	(NULL,"arroz","Yamani",1,0,0),(NULL,"arroz","Integral" ,2,0,0),
		(NULL,"azucar","Blanco",0.25,0,0),(NULL,"azucar","Moreno",0.5,0,0),
    	(NULL,"azucar","Refinado",1,0,0),(NULL,"azucar","Integral",2,0,0),
		(NULL,"sal","Marino",0.25,0,0),(NULL,"sal","Común",0.5,0,0),
    	(NULL,"sal","Kosher",1,0,0),(NULL,"sal","Himalaya",2,0,0)"""
		self.c.execute(borra)
		self.conex.commit()
		self.c.execute(insertar)
		self.conex.commit()
       	
	def consulta_productos(self):
		Konsultation=self.c.execute("SELECT * FROM PRODUCTOS")
		self.conex.commit()
		for  row_number, row_data in enumerate(Konsultation):
			self.tab_Almacen.insertRow(row_number)
			for colum_number, data in enumerate(row_data):   
				self.tab_Almacen.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))        
		self.c.close()
    	
    