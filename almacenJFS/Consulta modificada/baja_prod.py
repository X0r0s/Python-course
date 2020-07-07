import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog
from Formularios import baja_productos
from PyQt5 import uic

class bajaproductos(QDialog):
	def __init__(self):
		super().__init__()
		uic.loadUi("Formularios/baja_productos.ui", self)
		self.pb_Borrar.clicked.connect(self.borra_productos)
		self.conex=sqlite3.connect("ALMACEN.db")
		self.c=self.conex.cursor()
	def borra_productos(self):
		art=self.ln_Art.text()
		desc=self.ln_Desc.text()
		self.c.execute("DELETE FROM PRODUCTOS WHERE AT_ST=? and DT_ST=?",(art, desc))
		self.conex.commit()
		self.ln_Art.clear()
		self.ln_Desc.clear()
		self.c.close()