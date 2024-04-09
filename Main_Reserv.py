#Run_reserv.py

import re

from Gui_ui import Ui_Form
from Run_reserv import Reserv



from PySide2.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from PySide2.QtCore import Qt

from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

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
        self.row_tmp = None


        self.ui.tableWidget_2.cellDoubleClicked.connect(self.Modifi_rsv)
        self.ui.modif_btn_2.clicked.connect(self.Modifi_Base)

        self.ui.elim_btn_2.clicked.connect(self.Erase_Base)

        q = QSqlQuery()
        q.exec_("select * from productos")
        while q.next():
            id = q.value(0)#id
            codigo = q.value(1)#codigo
            nombre = q.value(2)#nombre
            modelo = q.value(3)#modelo
            datos = (id, codigo, nombre, modelo)
            self.NewRow_Table_Widget2(datos)

        self.Obtener_ID()
        
        self.ui.new_btn.clicked.connect(self.Insertar)



    def columnCount(self):
        #self.ui.tableWidget.columnCount()
        return self.ui.tableWidget.columnCount()

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

## OPT2
    def columnCount2(self):
        #self.ui.tableWidget_2.columnCount()
        return self.ui.tableWidget_2.columnCount()

    def rowCount2(self):
        return self.ui.tableWidget_2.rowCount()

    def NewRow_Table_Widget2(self, datos):
        row = self.rowCount2()
        self.ui.tableWidget_2.insertRow(row)
        #self.ui.tableWidget.verticalHeader().setVisible(False)
        for j in range(self.columnCount2()):
            item = QTableWidgetItem(str(datos[j]))
            self.ui.tableWidget_2.setItem(row, j, item)
### OPT2


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
    def Obtener_ID(self):
        q = QSqlQuery()
        sql = "SELECT id FROM productos ORDER BY id DESC"
        q.exec_(sql)

        if q.next():
            self.ID = q.value(0)
        else:
            self.ID = 0

        self.ui.lineEdit_txt.setText(str(self.ID))

    def getNew_ID(self):
        self.ID = str(int(self.ID)+1)
        return self.ID



    def Insertar(self):
        self.arg = (self.getNew_ID(), self.ui.codigo_txt.text(), self.ui.nombre_txt.text(), self.ui.modelo_txt.text())
        self.NewRow_Table_Widget2(self.arg)
        self.insertar_producto(*self.arg[1:])

    def Update_data(self, codigo, modelo,  nombre_producto):
        global db
        q = QSqlQuery()
        sql = """UPDATE productos SET CODIGO = {},     MODELO = {}, NOMBRE = {}   WHERE NOMBRE = {}""".format(codigo, modelo, nombre_producto,  nombre_producto)
        q.exec_(sql)
        db.commit()


    def Erase_Base(self):
        if self.row_tmp:
            item = self.ui.tableWidget_2.item(self.row_tmp, 0)#ID
            sql = "DELETE FROM productos WHERE id = {}".format(item.text())
            q = QSqlQuery()
            q.exec_(sql)
            self.ui.tableWidget_2.removeRow(self.row_tmp)
            self.row_tmp = None


    def Modifi_Base(self):
        if self.row_tmp is None:
            return

        datos = ("xxx", self.ui.codigo_txt.text(), self.ui.nombre_txt.text(), self.ui.modelo_txt.text())
        for j in range(1, self.columnCount2()):
            item = self.ui.tableWidget_2.item(self.row_tmp, j)
            item.setText(str(datos[j]))
            self.ui.tableWidget_2.setItem(self.row_tmp, j, item)

        self.Update_data(datos[1],   datos[3],    datos[2])
        self.insertar_producto(datos[1],   datos[2],    datos[3])
        self.row_tmp = None

    def Modifi_rsv(self, row, col):#Falta codigo!
        #Elem select -> row, col==1.   codigo, nombre, modelo, sqlquery()
        #item = self.ui.tableWidget_2.item(row, 1)# Nombre
        self.row_tmp = row
        datos = []
        for j in range(self.columnCount2()):
            item = self.ui.tableWidget_2.item(row, j)
            datos.append(item.text() if item else "")
        
        (print("ID:", datos[0]), 
            self.ui.codigo_txt.setText(datos[1]),
            self.ui.nombre_txt.setText(datos[2]), 
            self.ui.modelo_txt.setText(datos[3]))

        #self.actualiza_productos()


    def insertar_producto(self, codigo, nombre, modelo):
        sql = """INSERT INTO productos (CODIGO, NOMBRE, MODELO)
            VALUES(?, ?, ?)"""
        #cur.execute(sql).format(codigo, nombre, modelo)
        q = QSqlQuery()
        if q.prepare(sql):
            q.addBindValue(codigo)
            q.addBindValue(nombre)
            q.addBindValue(modelo)
            if q.exec_():
                print("Campo agregado satisfactoriamente!")



    def buscar_productos(self):
        sql = "SELECT * FROM productos"
        cur.execute(sql)

    def busca_producto(self, nombre):
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre)
        cur.execute(sql)

    def elimina_producto(self, nombre):
        sql = "DELETE FROM productos WHERE NOMBRE = {}".format(nombre)
        cur.execute(sql)


    def actualiza_productos(self, codigo, modelo, nombre_producto):#Via  Nombre
        sql = """UPDATE productos SET CODIGO = {},     MODELO = {}
            WHERE NOMBRE = {}""".format(codigo, modelo,  nombre_producto)
        cur.execute(sql)


def prepareDataBase():
    global db
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("data.db")

    if db.open():
        q = QSqlQuery()
        if q.prepare("create table if not exists  productos (id integer primary key autoincrement not null, CODIGO text not null, NOMBRE text not null, MODELO text not null )"):
            if q.exec_():
                print("TABLA  <productos>  creada satisfactoriamente!")
        db_create()

def db_create():
    query = QSqlQuery()
    # query.exec_("create table productos(id int primary key, "
    #             "CODIGO varchar(20), NOMBRE varchar(20), MODELO varchar(20))")
   
    ## prepareDataBase()
    query.exec_("insert into productos values(101, 'Cod13', 'viernes', '11')")
    query.exec_("insert into productos values(102, 'Cod13', 'viernes', '11')")
    query.exec_("insert into productos values(103, 'fir12', 'sara', '77')")
    query.exec_("insert into productos values(104, 'ir13', 'Sonia', '404')")


##

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    prepareDataBase()
    w = GUI()
    w.show()
    sys.exit(app.exec_())