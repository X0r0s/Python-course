# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifica_producto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_Consulta(object):
    def setupUi(self, form_Consulta):
        form_Consulta.setObjectName("form_Consulta")
        form_Consulta.resize(551, 555)
        self.tab_Almacen = QtWidgets.QTableWidget(form_Consulta)
        self.tab_Almacen.setGeometry(QtCore.QRect(10, 260, 531, 221))
        self.tab_Almacen.setRowCount(15)
        self.tab_Almacen.setColumnCount(5)
        self.tab_Almacen.setObjectName("tab_Almacen")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tab_Almacen.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tab_Almacen.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tab_Almacen.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tab_Almacen.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tab_Almacen.setHorizontalHeaderItem(4, item)
        self.pb_Consulta = QtWidgets.QPushButton(form_Consulta)
        self.pb_Consulta.setGeometry(QtCore.QRect(460, 500, 80, 24))
        self.pb_Consulta.setObjectName("pb_Consulta")
        self.pb_Salir = QtWidgets.QPushButton(form_Consulta)
        self.pb_Salir.setGeometry(QtCore.QRect(370, 500, 80, 24))
        self.pb_Salir.setObjectName("pb_Salir")
        self.pb_modifica = QtWidgets.QPushButton(form_Consulta)
        self.pb_modifica.setGeometry(QtCore.QRect(280, 150, 96, 27))
        self.pb_modifica.setObjectName("pb_modifica")
        self.Art = QtWidgets.QLineEdit(form_Consulta)
        self.Art.setGeometry(QtCore.QRect(30, 20, 113, 31))
        self.Art.setObjectName("Art")
        self.Desc = QtWidgets.QLineEdit(form_Consulta)
        self.Desc.setGeometry(QtCore.QRect(30, 60, 113, 31))
        self.Desc.setObjectName("Desc")
        self.Peso = QtWidgets.QLineEdit(form_Consulta)
        self.Peso.setGeometry(QtCore.QRect(30, 100, 113, 31))
        self.Peso.setObjectName("Peso")
        self.P_Unit = QtWidgets.QLineEdit(form_Consulta)
        self.P_Unit.setGeometry(QtCore.QRect(30, 180, 113, 31))
        self.P_Unit.setObjectName("P_Unit")
        self.Cant = QtWidgets.QLineEdit(form_Consulta)
        self.Cant.setGeometry(QtCore.QRect(30, 140, 113, 31))
        self.Cant.setObjectName("Cant")
        self.label = QtWidgets.QLabel(form_Consulta)
        self.label.setGeometry(QtCore.QRect(150, 30, 67, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(form_Consulta)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 81, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(form_Consulta)
        self.label_3.setGeometry(QtCore.QRect(150, 150, 67, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(form_Consulta)
        self.label_4.setGeometry(QtCore.QRect(150, 110, 67, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(form_Consulta)
        self.label_5.setGeometry(QtCore.QRect(150, 190, 67, 19))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(form_Consulta)
        self.pb_Salir.pressed.connect(form_Consulta.close)
        QtCore.QMetaObject.connectSlotsByName(form_Consulta)

    def retranslateUi(self, form_Consulta):
        _translate = QtCore.QCoreApplication.translate
        form_Consulta.setWindowTitle(_translate("form_Consulta", "Productos"))
        item = self.tab_Almacen.horizontalHeaderItem(0)
        item.setText(_translate("form_Consulta", "Artículo"))
        item = self.tab_Almacen.horizontalHeaderItem(1)
        item.setText(_translate("form_Consulta", "Descripción"))
        item = self.tab_Almacen.horizontalHeaderItem(2)
        item.setText(_translate("form_Consulta", "Peso"))
        item = self.tab_Almacen.horizontalHeaderItem(3)
        item.setText(_translate("form_Consulta", "Cantidad"))
        item = self.tab_Almacen.horizontalHeaderItem(4)
        item.setText(_translate("form_Consulta", "P Unit"))
        self.pb_Consulta.setText(_translate("form_Consulta", "Consulta"))
        self.pb_Salir.setText(_translate("form_Consulta", "Salir"))
        self.pb_modifica.setText(_translate("form_Consulta", "Modifcar"))
        self.label.setText(_translate("form_Consulta", "Articulo"))
        self.label_2.setText(_translate("form_Consulta", "Descripcion"))
        self.label_3.setText(_translate("form_Consulta", "Cantidad"))
        self.label_4.setText(_translate("form_Consulta", "Peso"))
        self.label_5.setText(_translate("form_Consulta", "P Unit"))
