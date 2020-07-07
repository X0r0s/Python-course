import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QAction, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon

class calc(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("calc_desc.ui",self)
		self.l_precio.text()
		self.l_desc.text()
		self.l_total.text()
		self.bt_acep.clicked.connect(self.calcular)
		self.des=100

	def calcular(self):
		self.l_total.setText(str(float(self.l_precio.text())-float(self.l_precio.text())*float(self.l_desc.text())/(self.des)))




if __name__=='__main__':
	app= QApplication(sys.argv)
	GUI=calc()
	GUI.show()
	sys.exit(app.exec())