"""
Formulario De Profesores

Jonathan Eliseo Dominguez Hdz.
GITI11071-E
Version 1.0

22/Octubre/2019
"""

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.Qt import QSqlDatabase
import sqlite3
from pprint import pprint


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(640, 515)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 50, 481, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ver_registro = QtWidgets.QPushButton(self.layoutWidget)
        self.ver_registro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ver_registro.setObjectName("ver_registro")
        self.verticalLayout.addWidget(self.ver_registro)
        self.Agregar = QtWidgets.QPushButton(self.layoutWidget)
        self.Agregar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Agregar.setObjectName("Agregar")
        self.verticalLayout.addWidget(self.Agregar)
        self.eliminar = QtWidgets.QPushButton(self.layoutWidget)
        self.eliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminar.setObjectName("eliminar")
        self.verticalLayout.addWidget(self.eliminar)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 631, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setGeometry(QtCore.QRect(10, 190, 611, 301))
        self.tableView.setObjectName("tableView")
        self.frame.raise_()
        self.label.raise_()
        self.layoutWidget.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

# CREACION DE LA BASE DE DATOS

        self.create_DB()
        self.ver_registro.clicked.connect(self.print_data)
        self.model = None
        self.ver_registro.clicked.connect(self.vizualisacion_tabla)
        self.Agregar.clicked.connect(self.agregar_registro)
        self.eliminar.clicked.connect(self.eliminar_registro)

# Funcion para eliminar registros

    def eliminar_registro(self):
            if self.model:
                self.model.removeRow(self.tableView.currentIndex().row())
            else:
                self.sql_tableview_model
       
# Funcion para agregar registros            
    def agregar_registro(self):
            if self.model:
                self.model.insertRows(self.model.rowCount(),1)
            else:
                self.sql_tableview_model()
        
# Funcion Para Visualizar los Registros en la Tabla                 
    def vizualisacion_tabla(self):
       
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('Profesores.db')
            
            tableview=self.tableView
            self.model= QtSql.QSqlTableModel()
            tableview.setModel(self.model)
            
            self.model.setTable('Profesores')
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Nombre")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Apellido")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Direccion")
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Telefono")
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Email")

# Funcion Para Visualizar los Registros en la Tabla

    def print_data(self):
            sqlite_file='Profesores.db'
            conn=sqlite3.connect(sqlite_file)
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM 'Profesores' ORDER BY id")
            all_rows = cursor.fetchall()
            pprint(all_rows)
            
            conn.commit()
            conn.close()
        
# Funcion Para Crear la Base de Datos
    
    def create_DB(self):
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('Profesores.db')
            db.open() 
            
            query = QtSql.QSqlQuery() 
            
            query.exec_("create table Profesores(id int primary key,"
                            "Nombre varchar(20), Apellido varchar(20), Direccion varchar(30), Telefono int(20), Email varchar(20))")
            query.exec_("insert into Profesores values(1, 'Jonathan', 'Dominguez', 'Miguel Hidalgo 42', '4181556335', 'jonas12gmail.com' )")
            query.exec_("insert into Profesores values(2, 'Jonas', 'Hernandez', 'Miguel Hidalgo 52', '4181556335', 'jonas12gmail.com' )")
            query.exec_("insert into Profesores values(3, 'Jose', 'Domingo', 'Miguel Hidalgo 40', '4181556335', 'jonas12gmail.com' )")
            query.exec_("insert into Profesores values(4, 'Juan', 'Cano', 'Miguel Hidalgo 46', '4181556335', 'jonas12gmail.com' )")


    def retranslateUi(self, mainWindow):
            _translate = QtCore.QCoreApplication.translate
            mainWindow.setWindowTitle(_translate("mainWindow", "Formulario de Profesores"))
            self.label.setText(_translate("mainWindow", "Formulario de Profesores"))
            self.ver_registro.setText(_translate("mainWindow", "Ver Registro"))
            self.Agregar.setText(_translate("mainWindow", "Agregar"))
            self.eliminar.setText(_translate("mainWindow", "Eliminar"))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
