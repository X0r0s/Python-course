import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class modificaproductos(QDialog):
	def __init__(self):
		super().__init__()
		uic.loadUi("Formularios/modifica_producto.ui", self)
		self.conex=sqlite3.connect("ALMACEN.db")
		self.c=self.conex.cursor()
		self.pb_Consulta.clicked.connect(self.consulta_productos)
		self.pb_modifica.clicked.connect(self.modifica_almacen)

	def consulta_productos(self):
		Konsultation=self.c.execute("SELECT * FROM PRODUCTOS")
		self.conex.commit()
		for  row_number, row_data in enumerate(Konsultation):
			self.tab_Almacen.insertRow(row_number)
			for colum_number, data in enumerate(row_data):   
				self.tab_Almacen.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))        
		self.c.close()


	def muestra_productos(mic,c):
		system("clear")

		try:
			c.execute("SELECT * FROM PRODUCTOS")
			lista = c.fetchall()
			mic.commit()
			print("Código\tArtículo\t\t\t\t\tDescripción\tPeso\tCantidad\t$ Unit")
			for i in lista:
				print( "%5d\t%7s\t%50s\t%4.2f\t%5d\t\t%5.2f" %(i[0], i[1], i[2], i[3], i[4],i[5]))
		except:   
			print ("Tabla no existe")

	def modifica_almacen(self):
		micon = sqlite3.connect("ALMACEN.db")
		cur = micon.cursor()
		ar1=[]
		ar2=[]


		try:
			muestra_productos(micon,cur)
		except:   
			print ("Tabla no existe")
	
		input("Esperá Carlo...")
		system("clear")
		print (" MODIFICA PRODUCTOS ")
   
		print (" Producto a modificar ")
   
		artviejo=input("   Artículo: ")
		desviejo=input("Descripción: ")

		artnuevo=input("   Artículo nuevo: ")
		desnuevo=input("Descripción nueva: ")
	

   
		ar1.append(artnuevo)
		ar1.append(desnuevo)
		ar1.append(artviejo)
		ar1.append(desviejo)
	
		peso=    input("    Peso nuevo: ")
		cant=    input("Unidades nuevo: ")
		valor=   input("   Valor nuevo: ")
		ar2.append(peso)
		ar2.append(cant)
		ar2.append(valor)
		ar2.append(artnuevo)
		ar2.append(desnuevo)


		print (ar1)
		print (ar2)
		input()

		
		modif1="""UPDATE PRODUCTOS 
		SET AT_ST=?, DT_ST=?
		WHERE AT_ST=? AND DT_ST=?"""

		modif2="""UPDATE PRODUCTOS 
		SET PS_ST=?, CN_ST=?, VL_ST=?
		WHERE AT_ST=? AND DT_ST=?"""
	   
		cur.execute(modif1,ar1)      
		micon.commit()
		cur.execute(modif2,ar2)      
		micon.commit()

		input("Esperá Carlo...")
		micon.close()

if __name__=='__main__':
	app= QApplication(sys.argv)
	movimientos=modificaproductos()
	movimientos.show()
	sys.exit(app.exec())
