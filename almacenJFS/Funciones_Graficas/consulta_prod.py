import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class consultaproductos(QDialog):
	def __init__(self):
		super().__init__()
		uic.loadUi("Formularios/consulta_productos.ui", self)
		self.conex=sqlite3.connect("ALMACEN.db")
		self.c=self.conex.cursor()
		self.pb_Consulta.clicked.connect(self.consulta_productos)
	def consulta_productos(self):
		Konsultation=self.c.execute("SELECT * FROM PRODUCTOS")
		self.conex.commit()
		for  row_number, row_data in enumerate(Konsultation):
			self.tab_Almacen.insertRow(row_number)
			for colum_number, data in enumerate(row_data):   
				self.tab_Almacen.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))        
		self.c.close()