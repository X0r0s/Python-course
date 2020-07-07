# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baja_productos.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog 
class Ui_Bajar_Prod(object):
    def setupUi(self, Bajar_Prod):
        Bajar_Prod.setObjectName("Bajar_Prod")
        Bajar_Prod.resize(382, 107)
        self.gridLayout_2 = QtWidgets.QGridLayout(Bajar_Prod)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lb_Tit = QtWidgets.QLabel(Bajar_Prod)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lb_Tit.setFont(font)
        self.lb_Tit.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_Tit.setObjectName("lb_Tit")
        self.gridLayout.addWidget(self.lb_Tit, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.lb_Art = QtWidgets.QLabel(Bajar_Prod)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lb_Art.setFont(font)
        self.lb_Art.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_Art.setObjectName("lb_Art")
        self.gridLayout.addWidget(self.lb_Art, 1, 1, 1, 1)
        self.ln_Art = QtWidgets.QLineEdit(Bajar_Prod)
        self.ln_Art.setObjectName("ln_Art")
        self.gridLayout.addWidget(self.ln_Art, 1, 2, 1, 1)
        self.pb_Borrar = QtWidgets.QPushButton(Bajar_Prod)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_Borrar.setFont(font)
        self.pb_Borrar.setObjectName("pb_Borrar")
        self.gridLayout.addWidget(self.pb_Borrar, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.lb_Desc = QtWidgets.QLabel(Bajar_Prod)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lb_Desc.setFont(font)
        self.lb_Desc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_Desc.setObjectName("lb_Desc")
        self.gridLayout.addWidget(self.lb_Desc, 2, 1, 1, 1)
        self.ln_Desc = QtWidgets.QLineEdit(Bajar_Prod)
        self.ln_Desc.setObjectName("ln_Desc")
        self.gridLayout.addWidget(self.ln_Desc, 2, 2, 1, 1)
        self.pb_Salir = QtWidgets.QPushButton(Bajar_Prod)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_Salir.setFont(font)
        self.pb_Salir.setObjectName("pb_Salir")
        self.gridLayout.addWidget(self.pb_Salir, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Bajar_Prod)
        self.pb_Salir.pressed.connect(Bajar_Prod.close)
        QtCore.QMetaObject.connectSlotsByName(Bajar_Prod)

    def retranslateUi(self, Bajar_Prod):
        _translate = QtCore.QCoreApplication.translate
        Bajar_Prod.setWindowTitle(_translate("Bajar_Prod", "Baja de Productos"))
        self.lb_Tit.setText(_translate("Bajar_Prod", "Baja de Productos"))
        self.lb_Art.setText(_translate("Bajar_Prod", "Artículo:"))
        self.pb_Borrar.setText(_translate("Bajar_Prod", "Borrar"))
        self.lb_Desc.setText(_translate("Bajar_Prod", "Descripción:"))
        self.pb_Salir.setText(_translate("Bajar_Prod", "Salir"))

if __name__=='__main__':
	app= QApplication(sys.argv)
	movimientos=Ui_Bajar_Prod()
	movimientos.show()
	sys.exit(app.exec())