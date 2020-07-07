import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class altaproductos(QDialog):
	def __init__(self):
		super().__init__()
		uic.loadUi("Formularios/alta_productos.ui", self)
		self.pb_Guardar.clicked.connect(self.agrega_productos)
		self.conex=sqlite3.connect("ALMACEN.db")
		self.c=self.conex.cursor()
		
	def agrega_productos(self):
		art=self.ln_Art.text()
		desc=self.ln_Desc.text()
		peso=float(self.ln_Peso.text())
		cant=int(self.ln_Cant.text())
		preciounit=float(self.ln_Precio_Unit.text())
		self.c.execute("INSERT INTO PRODUCTOS VALUES (NULL, ?,?,?,?,?)",(art,desc,peso,cant,preciounit))
		self.conex.commit()
		self.c.close()
		
if __name__=='__main__':
	app= QApplication(sys.argv)
	movimientos=altaproductos()
	movimientos.show()
	sys.exit(app.exec())		