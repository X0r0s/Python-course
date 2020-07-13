# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

def crear_db(db_name):
    connection = sqlite3.connect(db_name + ".db")
    connection.close()
    print (db_name + " Ha sido Creada!")



class Ui_DataWindow(object):
    def setupUi(self, DataWindow):
        DataWindow.setObjectName("DataWindow")
        DataWindow.resize(678, 434)
        self.centralwidget = QtWidgets.QWidget(DataWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 651, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ld_db_create = QtWidgets.QLineEdit(self.centralwidget)
        self.ld_db_create.setGeometry(QtCore.QRect(220, 150, 261, 31))
        self.ld_db_create.setAlignment(QtCore.Qt.AlignCenter)
        self.ld_db_create.setObjectName("ld_db_create")
        self.btn_db_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_db_create.setGeometry(QtCore.QRect(300, 190, 111, 31))
        self.btn_db_create.setObjectName("btn_db_create")
        ###########################################################################
        #utilizo el lambda para poder pasar los argumentos contenidos en el def de manera mas rapida.
        self.btn_db_create.clicked.connect(lambda : crear_db(self.ld_db_create.text()))
        ###########################################################################
        DataWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DataWindow)
        self.statusbar.setObjectName("statusbar")
        DataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DataWindow)
        QtCore.QMetaObject.connectSlotsByName(DataWindow)

    def retranslateUi(self, DataWindow):
        _translate = QtCore.QCoreApplication.translate
        DataWindow.setWindowTitle(_translate("DataWindow", "MainWindow"))
        self.label.setText(_translate("DataWindow", "PyQt Database"))
        self.ld_db_create.setPlaceholderText(_translate("DataWindow", "Database Name"))
        self.btn_db_create.setText(_translate("DataWindow", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataWindow = QtWidgets.QMainWindow()
    ui = Ui_DataWindow()
    ui.setupUi(DataWindow)
    DataWindow.show()
    sys.exit(app.exec_())

