#Run_reserv.py

import re

from Gui_ui import Ui_Form
from Run_reserv import Reserv



from PySide2.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from PySide2.QtCore import Qt

from PySide2.QtSql import QSqlDatabase, QSqlQuery

# class ClassName(Ui_Dialog, QDialog):
#     """docstring for ClassName"""
#     def __init__(self):
#         super(ClassName, self).__init__()
#         super(ClassName, self).setupUi(self)
#         self.arg = None



class GUI(QWidget):
    """docstring for GUI"""
    def __init__(self):
        super(GUI, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.cellDoubleClicked.connect(self.modif_reserv)
        self.ui.nuevo_btn.clicked.connect(self.nueva_reserv)
        self.arg = None

    def columnCount(self):
        #self.ui.tableWidget.columnCount()
        return 7

    def rowCount(self):
        return self.ui.tableWidget.rowCount()

    def NewRow_Table_Widget(self, datos):
        row = self.rowCount()
        self.ui.tableWidget.insertRow(row)
        #self.ui.tableWidget.verticalHeader().setVisible(False)
        for col in range(self.columnCount()):
            item = QTableWidgetItem(str(datos[col]))
            self.ui.tableWidget.setItem(row, col, item)
            self.ui.lineEdit_txt.setText(str(datos[0]))

    def datos_TableWidget(self, row, col):
        data = []
        for j in range(self.columnCount()):
            item = self.ui.tableWidget.item(row, j)
            data.append(item.text() if item else "")
            self.ui.lineEdit_txt.setText(str(data)+"Hello")
        return data

    def modif_reserv(self, row, col):
        self.ui.lineEdit_txt.setText(str(27)+str(self.arg))
        # row = new.row()
        # col = new.column()
        # data = new.text()
        self.arg = self.datos_TableWidget(row, col)
        w = Reserv(self.arg)
        w.show()
        w.exec_()
        # if w.exec_() == Qt.Accepted:
        #     #Modif Database
        #     print("Modif Database")
        # else:
        #     pass

    def nueva_reserv(self, new=None):
        self.arg = (self.rowCount(), "Maria", "3", "8/04/2024", "DEGRADE                                     $3000", "$3000", "")
        self.NewRow_Table_Widget(self.arg)
        #self.ui.lineEdit_txt.setText("Hi")
        # w = Reserv()
        # w.show()
        # if w.exec_() == Qt.Accepted:
        #     #Nuevo Elemento en la Database
        #     print("Nuevo Elemento en la Database")
        # else:
        #     pass

##  Preparar Base de Datos
    def insertar_producto(self):
        sql = """INSERT INTO productos (CODIGO, NOMBRE, MODELO)
            VALUES('{}', '{}', '{}')""".format(codigo, nombre, modelo)
        cur.execute(sql)

    def buscar_productos(self):
        sql = "SELECT * FROM productos"
        cur.execute(sql)

    def busca_producto(self):
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre)
        cur.execute(sql)

    def elimina_producto(self):
        sql = "DELETE FROM productos WHERE NOMBRE = {}".format(nombre)
        cur.execute(sql)


    def actualiza_productos(self):
        sql = """UPDATE productos SET CODIGO = {},  MODELO = {}
            WHERE NOMBRE = {}""".format(codigo, modelo,  nombre_producto)
        cur.execute(sql)


def prepareDataBase():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("data.db")

    if db.open():
        q = QSqlQuery()
        if q.prepare("create table if not exists  productos (id integer primary key autoincrement not null, CODIGO text not null, NOMBRE text not null, MODELO text not null )"):
            if q.exec_():
                print("TABLA  <productos>  creada satisfactoriamente!")

##

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    prepareDataBase()
    w = GUI()
    w.show()
    sys.exit(app.exec_())