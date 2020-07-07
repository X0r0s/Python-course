# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_Salir = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Salir.setGeometry(QtCore.QRect(20, 510, 80, 24))
        self.pb_Salir.setObjectName("pb_Salir")
        Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAlmacen = QtWidgets.QMenu(self.menubar)
        self.menuAlmacen.setObjectName("menuAlmacen")
        self.menuMovimientos_de_Mercaderia = QtWidgets.QMenu(self.menubar)
        self.menuMovimientos_de_Mercaderia.setObjectName("menuMovimientos_de_Mercaderia")
        Principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)
        self.actionCarga_Inicial = QtWidgets.QAction(Principal)
        self.actionCarga_Inicial.setObjectName("actionCarga_Inicial")
        self.actionMuestra_Producto = QtWidgets.QAction(Principal)
        self.actionMuestra_Producto.setObjectName("actionMuestra_Producto")
        self.actionModifica_Producto = QtWidgets.QAction(Principal)
        self.actionModifica_Producto.setObjectName("actionModifica_Producto")
        self.actionSalir = QtWidgets.QAction(Principal)
        self.actionSalir.setObjectName("actionSalir")
        self.actionVentas = QtWidgets.QAction(Principal)
        self.actionVentas.setObjectName("actionVentas")
        self.actionAltas = QtWidgets.QAction(Principal)
        self.actionAltas.setObjectName("actionAltas")
        self.actionConsultas = QtWidgets.QAction(Principal)
        self.actionConsultas.setObjectName("actionConsultas")
        self.actionModificaciones = QtWidgets.QAction(Principal)
        self.actionModificaciones.setObjectName("actionModificaciones")
        self.actionBajas = QtWidgets.QAction(Principal)
        self.actionBajas.setObjectName("actionBajas")
        self.menuAlmacen.addSeparator()
        self.menuAlmacen.addAction(self.actionCarga_Inicial)
        self.menuAlmacen.addAction(self.actionMuestra_Producto)
        self.menuAlmacen.addAction(self.actionModifica_Producto)
        self.menuAlmacen.addAction(self.actionSalir)
        self.menuMovimientos_de_Mercaderia.addAction(self.actionVentas)
        self.menuMovimientos_de_Mercaderia.addAction(self.actionAltas)
        self.menuMovimientos_de_Mercaderia.addAction(self.actionModificaciones)
        self.menuMovimientos_de_Mercaderia.addAction(self.actionBajas)
        self.menubar.addAction(self.menuAlmacen.menuAction())
        self.menubar.addAction(self.menuMovimientos_de_Mercaderia.menuAction())

        self.retranslateUi(Principal)
        self.pb_Salir.pressed.connect(Principal.close)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Principal"))
        self.pb_Salir.setText(_translate("Principal", "Salir"))
        self.menuAlmacen.setTitle(_translate("Principal", "Almacen"))
        self.menuMovimientos_de_Mercaderia.setTitle(_translate("Principal", "Movimientos de Mercaderia"))
        self.actionCarga_Inicial.setText(_translate("Principal", "Carga Inicial"))
        self.actionMuestra_Producto.setText(_translate("Principal", "Muestra Producto"))
        self.actionModifica_Producto.setText(_translate("Principal", "Modifica Producto"))
        self.actionSalir.setText(_translate("Principal", "Salir"))
        self.actionVentas.setText(_translate("Principal", "Ventas"))
        self.actionAltas.setText(_translate("Principal", "Altas"))
        self.actionConsultas.setText(_translate("Principal", "Consultas"))
        self.actionModificaciones.setText(_translate("Principal", "Modificaciones"))
        self.actionBajas.setText(_translate("Principal", "Bajas"))

