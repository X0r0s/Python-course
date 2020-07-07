import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QAction, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from inicia_almacen import creaalmacen
from alta_prod import altaproductos
from consulta_prod import consultaproductos
from baja_prod import bajaproductos
from modifica_prod import modificaproductos


class ventana1 (QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("Formularios/ventana1.ui",self)
		self.conex=sqlite3.connect("ALMACEN.db")
		self.c=self.conex.cursor()
		self.actionCarga_Inicial.triggered.connect(self.inicia_producto)
		self.actionMuestra_Producto.triggered.connect(self.consulta_producto)
		self.actionModifica_Producto.triggered.connect(self.modifica_producto)
		self.actionSalir.triggered.connect(self.salir_apli)

		self.actionAltas.triggered.connect(self.alta_productos)
		self.actionBajas.triggered.connect(self.baja_productos)
		
	def inicia_producto(self):
		creaalmacen().exec_()	
	def consulta_producto(self):
		consultaproductos().exec_()
	def modifica_producto(self):
		modificaproductos().exec_()
	
	def salir_apli(self):
		sys.exit(app.exec())

	def alta_productos(self):
		altaproductos().exec_()
	def baja_productos(self):
		bajaproductos().exec_()	
	
		

if __name__=='__main__':
	app= QApplication(sys.argv)
	movimientos=ventana1()
	movimientos.show()
	sys.exit(app.exec())