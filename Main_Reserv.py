#Run_reserv.py

import re

from Gui_ui import Ui_Form
from Run_reserv import Reserv
from Run_buscar import _Buscar



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
        self.arg = None
        self.row_tmp = None
        
        self.ui.nuevo_btn.clicked.connect(self.nueva_reserv)
        self.ui.modif_btn.clicked.connect(self.modif_row)
        self.ui.tableWidget.cellDoubleClicked.connect(self.modif_reserv)
        self.ui.elim_btn.clicked.connect(self.Eliminar_Reserv)


        self.ui.buscar_btn.clicked.connect(self.buscar_Reserv)

        q = QSqlQuery()
        q.exec_("select * from Reserv_Clientes")
        while q.next():
            datos = [q.value(i) for i in range(self.columnCount())]
            self.NewRow_Table_Widget(datos)

## tableWidget_2
        q = QSqlQuery()
        q.exec_("select * from productos")
        while q.next():
            id = q.value(0)#id
            codigo = q.value(1)#codigo
            nombre = q.value(2)#nombre
            modelo = q.value(3)#modelo
            datos = (id, codigo, nombre, modelo)
            self.NewRow_Table_Widget2(datos)
##

        self.Obtener_ID()
        self.Obtener_ID2()
        
        self.ui.new_btn.clicked.connect(self.Insertar)
        self.ui.tableWidget_2.cellDoubleClicked.connect(self.Modifi_rsv)
        self.ui.modif_btn_2.clicked.connect(self.Modifi_Base)

        self.ui.elim_btn_2.clicked.connect(self.Erase_Base)



    def Obtener_ID(self):
        q = QSqlQuery()
        sql = "SELECT id FROM Reserv_Clientes ORDER BY id DESC"
        q.exec_(sql)

        if q.next():
            self.ID = q.value(0)
        else:
            self.ID = 0

        self.ui.lineEdit_txt.setText("ID: "+str(self.ID))

    def getNew_ID(self):
        self.ID = str(int(self.ID)+1)
        return self.ID

    def TableWidget(self):
        return self.ui.tableWidget

    def selectRow(self, row):
        print("selectRow", row)
        return self.ui.tableWidget.selectRow(row)


    def columnCount(self):
        #self.ui.tableWidget.columnCount()
        return self.ui.tableWidget.columnCount()

    def rowCount(self):
        return self.ui.tableWidget.rowCount()

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
            item.setFlags(item.flags()^Qt.ItemIsEditable)
            self.ui.tableWidget_2.setItem(row, j, item)

### OPT2

    def datos_TableWidget(self, row):
        data = []
        for j in range(self.columnCount()):
            item = self.ui.tableWidget.item(row, j)
            data.append(item.text() if item else "")
        return data


    def NewRow_Table_Widget(self, datos):
        row = self.rowCount()
        self.ui.tableWidget.insertRow(row)
        #self.ui.tableWidget.verticalHeader().setVisible(False)
        for col in range(self.columnCount()):
            item = QTableWidgetItem(str(datos[col]))
            item.setFlags(item.flags()^Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(row, col, item)
            self.ui.lineEdit_txt.setText("New ID: "+str(datos[0]))## print New ID

    def Modif_Table_Widget(self, row, datos):
        for j in range(self.columnCount()):
            item = self.ui.tableWidget.item(row, j)
            print("row, j", row, j)
            if item is None: #caso particular
                item = QTableWidgetItem()
            item.setText(datos[j])
            self.ui.tableWidget.setItem(row, j, item)##parece innecesario



    def nueva_reserv(self, new=None):
        datos = ["", "Maria", "3", "8/04/2024", "DEGRADE                                     $3000", "$3000", ""]
        
        w = Reserv(datos, 0)
        w.show()
        if w.exec_() == Reserv.Accepted:
            print("Nuevo Elemento en la Database")

            datos = w.get_data()
            datos[0] = self.getNew_ID()
            self.NewRow_Table_Widget(datos)
            self.insertar_data(datos)


    def modif_row(self):
        TwItems = self.ui.tableWidget.selectedItems()
        if TwItems:
            row = TwItems[0].row()
            col = TwItems[0].column()
            self.modif_reserv(row, col)


    def modif_reserv(self, row, col):
        datos = self.datos_TableWidget(row)
        self.ui.lineEdit_txt.setText(str(27)+str(datos))
        w = Reserv(datos, 1)
        w.show()
        if w.exec_() == Reserv.Accepted:
            #Modif Database
            datos = w.get_data()
            if datos[0] is "":
                datos[0] = self.getNew_ID()
                self.insertar_data(datos)### fase de prueba. TwItem == None.
                print("Insertar Database")
            else:
                print("Modif Database")
                self.actualizar_data(datos)
            self.Modif_Table_Widget(row, datos)


    def Eliminar_Reserv(self):
        TwItems = self.ui.tableWidget.selectedItems()
        if not TwItems:
            print("Eliminar_Reserv Not SelectedItems!")
            return
        if TwItems:### w = Reserv(datos, 2)
            datos = self.datos_TableWidget(TwItems[0].row())##row
            w = Reserv(datos, 2)
            w.show()
            if w.exec_() == Reserv.Accepted:

                row = TwItems[0].row()
                item = self.ui.tableWidget.item(row, 0)#ID
                self.remover_data(item)
                self.ui.tableWidget.removeRow(row)


    def insertar_data(self, datos):
        sql = """INSERT INTO Reserv_Clientes (  NOMBRE, Cod_clie, fecha, Trabajos, precio , Observaciones)
            VALUES(?, ?, ?, ?, ?, ?)"""
        q = QSqlQuery()
        if q.prepare(sql):
            for i in range(1, self.columnCount()):
                q.addBindValue(datos[i])
            q.exec_()

    def actualizar_data(self, datos):
        self.ui.lineEdit_txt.setText(str(datos)+str(11))
        print("datos[1:] ", datos[1:], len(datos), "\n\n")
        q = QSqlQuery()
        sql = "UPDATE Reserv_Clientes SET NOMBRE = '%s', Cod_clie = '%s', fecha = '%s', Trabajos = '%s', precio = '%s' , Observaciones = '%s'    WHERE id = %s "%(*datos[1:],  datos[0])
        q.exec_(sql)
        if not q.isActive():
            self.ui.lineEdit_txt.setText("Fallo  actualizar_data()")

    def remover_data(self, item):
        sql = "DELETE FROM Reserv_Clientes WHERE id = {}".format(item.text())
        q = QSqlQuery()
        q.exec_(sql)


    def buscar_Reserv(self):
        w = _Buscar()
        w.setGridParent(self)
        w.show()
        if w.exec_() == _Buscar.Accepted:
            #_Buscar Database
            print("_Buscar Database Cerrado")


##  Preparar Base de Datos
    def Obtener_ID2(self):
        q = QSqlQuery()
        sql = "SELECT id FROM productos ORDER BY id DESC"
        q.exec_(sql)

        if q.next():
            self.ID2 = q.value(0)
        else:
            self.ID2 = 0

        self.ui.lineEdit_txt.setText("ID2: "+str(self.ID2))

    def getNew_ID2(self):
        self.ID2 = str(int(self.ID2)+1)
        return self.ID2

    def Insertar(self):
        datos = (self.getNew_ID2(), self.ui.codigo_txt.text(), self.ui.nombre_txt.text(), self.ui.modelo_txt.text())
        self.NewRow_Table_Widget2(datos)
        self.insertar_producto(*datos[1:])


    def Erase_Base(self):
        if self.row_tmp:
            item = self.ui.tableWidget_2.item(self.row_tmp, 0)#ID
            sql = "DELETE FROM productos WHERE id = {}".format(item.text())
            q = QSqlQuery()
            q.exec_(sql)
            self.ui.tableWidget_2.removeRow(self.row_tmp)
            self.row_tmp = None


    def Update_data(self, codigo, modelo,  nombre_producto, id):
        global db
        q = QSqlQuery()
        sql = """UPDATE productos SET CODIGO = '%s',     MODELO = '%s', NOMBRE = '%s'   WHERE id = %s """%(codigo, modelo, nombre_producto,  id)
        q.exec_(sql)
        db.commit()
        if not q.isActive():
            self.ui.lineEdit_txt.setText("Fallo  Update_data()")



    def Modifi_Base(self):
        if self.row_tmp is None:
            return

        datos = ("xxx", self.ui.codigo_txt.text(), self.ui.nombre_txt.text(), self.ui.modelo_txt.text())
        for j in range(1, self.columnCount2()):
            item = self.ui.tableWidget_2.item(self.row_tmp, j)
            item.setText(str(datos[j]))
            self.ui.tableWidget_2.setItem(self.row_tmp, j, item)

        self.Update_data(datos[1],   datos[3],    datos[2],    self.ui.tableWidget_2.item(self.row_tmp, 0).text())
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

        q = QSqlQuery()
        if q.prepare(sql):
            q.addBindValue(codigo)
            q.addBindValue(nombre)
            q.addBindValue(modelo)
            if q.exec_():
                print("Campo agregado satisfactoriamente!")



def prepareDataBase():
    global db
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("data.db")

    if db.open():
        q = QSqlQuery()
        if q.prepare("create table if not exists  productos (id integer primary key autoincrement not null, CODIGO text not null, NOMBRE text not null, MODELO text not null )"):
            if q.exec_():
                print("TABLA  <productos>  creada satisfactoriamente!")

        q = QSqlQuery()
        if q.prepare("create table if not exists  Reserv_Clientes (id integer primary key autoincrement not null, NOMBRE text not null, Cod_clie text, fecha text not null, Trabajos text not null, precio text not null , Observaciones text not null )"):
            if q.exec_():
                print("TABLA  <Reserv_Clientes>  creada satisfactoriamente!")
        db_create()
        q = QSqlQuery()
        if q.prepare("create table if not exists  Reserv_data (id integer primary key autoincrement not null, Cod_clie text, fecha text not null, path text not null )"):
            if q.exec_():
                print("TABLA  <Reserv_data>  creada satisfactoriamente!")
        Registro_db_create()

def db_create():
    query = QSqlQuery()
    ## prepareDataBase()
    query.exec_("insert into productos values(101, 'Cod13', 'viernes', '11')")
    query.exec_("insert into productos values(102, 'Cod13', 'viernes', '11')")
    query.exec_("insert into productos values(103, 'fir12', 'sara', '77')")
    query.exec_("insert into productos values(104, 'ir13', 'Sonia', '404')")


def Registro_db_create():
    query = QSqlQuery()
    query.exec_("insert into Reserv_data values(111, '1', '5/04/2024' , 'C:/Users/FernandezMiguelA/Downloads/Gestor_remake/Imagenes/img_1.png')")
    query.exec_("insert into Reserv_data values(112, '2', '10/04/2024', 'C:/Users/FernandezMiguelA/Downloads/Gestor_remake/Imagenes/img_2.png')")
    query.exec_("insert into Reserv_data values(113, '3', '12/04/2024', 'C:/Users/FernandezMiguelA/Downloads/Gestor_remake/Imagenes/img_3.png')")


##

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    prepareDataBase()
    w = GUI()
    w.show()
    sys.exit(app.exec_())