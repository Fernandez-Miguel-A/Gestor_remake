#Run_reserv.py

import re

from Gui_ui import Ui_Form
from Run_reserv import Reserv
from Run_buscar import _Buscar

from pyDrillDown.connection import create_connection
from pyDrillDown.libs.grapichsitem import GItem


from PySide6.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from PySide6.QtCore import Qt

from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

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

        database = create_connection()
        self.ui.graphicsView.set_database(database)
        ## self.ui.graphicsView.add_DefaultItems() ## 'Ahora' ignoro los GItems vacios
        
        self.ui.nuevo_btn.clicked.connect(self.nueva_reserv)
        self.ui.modif_btn.clicked.connect(self.modif_row)
        self.ui.tableWidget.cellDoubleClicked.connect(self.modif_TWreserv)
        self.ui.elim_btn.clicked.connect(self.Eliminar_Reserv_data)


        self.ui.buscar_btn.clicked.connect(self.buscar_Reserv)

        self.ui.chk_Todos.toggled.connect(lambda x: self.ui.dateEdit.setEnabled(not x))
        self.ui.chk_Todos.toggled.connect(self.UpdateTotalView)
        self.ui.dateEdit.userDateChanged.connect(self.UpdateTotalView)
        
        self.ui.graphicsView.hide()
        self.ui.View_Table.toggled.connect(lambda x,this=self.ui: (this.graphicsView.setVisible(x), this.tabWidget.setVisible(not x)))
        self.ui.graphicsView.GItemPressed.connect(self.modifGItem)

        self.UpdateTotalView()

## tableWidget_2
        q = QSqlQuery()
        q.exec("select * from productos")
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
        q.exec(sql)

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


    def columnCountTW(self):
        return self.ui.tableWidget.columnCount()

    def rowCountTW(self):
        return self.ui.tableWidget.rowCount()

    def Reserv_CountData(self):
        """supongo que siempre cargare todos los datos de la BASE de DATOS en la TableWidget y GView"""
        return self.columnCountTW()

    def UpdateTotalView(self):
        print("UpdateTotalView")
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        self.ui.graphicsView.clearGItems()
        ## borro todos los campos y luego cargo los particulares
    #   self.MakeReservClie()

        query = QSqlQuery()
        if self.ui.chk_Todos.checkState() == Qt.CheckState.Checked:
            if not query.exec("SELECT * FROM Reserv_Clientes"):
                self.ui.lineEdit_txt.setText(
                    f"Fallo al cargar reservas: {query.lastError().text()}"
                )
                return
            while query.next():
                datos = [query.value(i) for i in range(self.Reserv_CountData())]
                self.MakeReservClie(datos)
            return

        if not query.prepare("SELECT * FROM Reserv_Clientes WHERE fecha = ?"):
            self.ui.lineEdit_txt.setText(
                f"Fallo al preparar consulta semanal: {query.lastError().text()}"
            )
            return

        selected_date = self.ui.dateEdit.date()
        week_start = selected_date.addDays(1 - selected_date.dayOfWeek())
        for day_offset in range(7):
            date = week_start.addDays(day_offset).toString("d/M/yyyy")
            query.bindValue(0, date)
            if not query.exec():
                self.ui.lineEdit_txt.setText(
                    f"Fallo al consultar {date}: {query.lastError().text()}"
                )
                return
            while query.next():
                datos = [query.value(i) for i in range(self.Reserv_CountData())]
                self.MakeReservClie(datos)



    def MakeReservClie(self, datos):
        print("MakeReservClie::", datos)
        self.NewRow_Table_Widget(datos)
        self.ui.graphicsView.addGItem(datos)

    def UpdateReservClie(self, row, datos):
        self.Modif_Table_Widget(row, datos)
        self.ui.graphicsView.UpdateGItem(datos)

    def RemoveReservClie(self, row, datos):
        self.ui.tableWidget.removeRow(row)
        self.ui.graphicsView.removeGItem(datos)


    def datos_TableWidget(self, row) -> list:
        data = []
        for j in range(self.Reserv_CountData()):
            item = self.ui.tableWidget.item(row, j)
            data.append(item.text() if item else "")

        data[0] = int(data[0]) ## 'id'
        data[2] = int(data[2]) ## 'cod_clie'
        return data


    def NewRow_Table_Widget(self, datos):
        row = self.rowCountTW()
        self.ui.tableWidget.insertRow(row)
        #self.ui.tableWidget.verticalHeader().setVisible(False)
        for col in range(self.columnCountTW()):
            item = QTableWidgetItem(str(datos[col])) ## 'id' y 'cod_clie' son 'int'
            item.setFlags(item.flags()^Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(row, col, item)
            self.ui.lineEdit_txt.setText("New ID: "+str(datos[0]))## print New ID

    def Modif_Table_Widget(self, row, datos): ## FIX-ED: "QTableWidget: ..
        new = False
        print("\n\n\n Modif_Table_Widget", self.columnCountTW(), row, datos)
        for j in range(self.columnCountTW()):
            item = self.ui.tableWidget.item(row, j)
            print("row, j", row, j, item)
            if item is None: #caso particular
                item = QTableWidgetItem()
                new = True
            item.setText(str(datos[j])) ## 'id' y 'cod_clie' son 'int'
            if new: ## FIX-ED: "QTableWidget: ..
                self.ui.tableWidget.setItem(row, j, item)

    def getRowfromID(self, id : int) -> int:
        print("getRowfromID:", id)
        for row in range(self.rowCountTW()):
            item = self.ui.tableWidget.item(row, 0)
            if isinstance(item, QTableWidgetItem) and item.text() == str(id):
                return row
        return -1



    def nueva_reserv(self, new=None):
        datos = [None, "Maria", 3, "8/04/2024", "DEGRADE                                     $3000", "$3000", ""]
        
        w = Reserv(self.ui.graphicsView, datos)
        ##w.setView()
        w.show()
        if w.exec() == Reserv.Accepted:
            print("Nuevo Elemento en la Database")

            datos = w.get_data()
            datos[0] = self.getNew_ID()
            self.MakeReservClie(datos)
            self.insertar_data(datos)


    def modif_row(self):
        TwItems = self.ui.tableWidget.selectedItems()
        if TwItems:
            row = TwItems[0].row()
            col = TwItems[0].column()
            self.modif_TWreserv(row, col)


    def modif_reserv(self, row, datos):
        self.ui.lineEdit_txt.setText(str(27)+str(datos))
        w = Reserv(self.ui.graphicsView, datos, Reserv.MODIF)
        w.show()
        if w.exec() == Reserv.Accepted:
            #Modif Database
            datos = w.get_data()
            if datos[0] == "" or datos[0] == None:
                print("Insertar Database")
                datos[0] = self.getNew_ID()
                self.insertar_data(datos)### fase de prueba. TwItem == None.
            else:
                print("Modif Database")
                self.actualizar_data(datos)
            self.UpdateReservClie(row, datos)


    def modif_TWreserv(self, row, col):
        datos = self.datos_TableWidget(row)
        self.modif_reserv(row, datos)

    def modifGItem(self, item):
        datos = item.model()
        idx = item.getGID()
        row = self.getRowfromID(idx)#datos[0]
        print("\n modifGItem::", idx, row, datos)
        self.modif_reserv(row, datos)
        


    def Eliminar_Reserv(self, item, row, datos):
        w = Reserv(self.ui.graphicsView, datos, Reserv.DEL)
        w.show()
        if w.exec() == Reserv.Accepted:
            id = datos[0]#ID
            self.remover_data(id)  ## CUIDADO
            self.RemoveReservClie(row, datos)

    def Eliminar_ReservTW(self):
        TwItems = self.ui.tableWidget.selectedItems()
        if not TwItems:
            print("Eliminar_ReservTW Not SelectedItems!")
            return
        item = TwItems[0]
        row = item.row()
        datos = self.datos_TableWidget(row)##row
        self.Eliminar_Reserv(item, row, datos)


    def Eliminar_ReservGW(self):
        TwItems = self.ui.graphicsView.selectedGItems()
        if not TwItems:
            print("Eliminar_ReservGW Not SelectedItems!")
            return
        item = TwItems[0]
        idx = item.getGID()
        row = self.getRowfromID(idx)
        datos = item.model()##row
        self.Eliminar_Reserv(item, row, datos)

    def Eliminar_Reserv_data(self):
        state = self.ui.View_Table.checkState()
        if state == Qt.Unchecked:
            self.Eliminar_ReservTW()
        else:
            self.Eliminar_ReservGW()


    def insertar_data(self, datos):
        sql = """INSERT INTO Reserv_Clientes (  NOMBRE, Cod_clie, fecha, Trabajos, precio , Observaciones)
            VALUES(?, ?, ?, ?, ?, ?)"""
        q = QSqlQuery()
        if q.prepare(sql):
            for i in range(1, self.Reserv_CountData()):
                q.addBindValue(datos[i])
            q.exec()

    def actualizar_data(self, datos):
        self.ui.lineEdit_txt.setText(str(datos)+str(11))
        q = QSqlQuery()
        sql = """UPDATE Reserv_Clientes
            SET NOMBRE = ?, Cod_clie = ?, fecha = ?, Trabajos = ?,
                precio = ?, Observaciones = ?
            WHERE id = ?"""
        if not q.prepare(sql):
            self.ui.lineEdit_txt.setText(
                f"Fallo actualizar_data(): {q.lastError().text()}"
            )
            return
        for value in datos[1:]:
            q.addBindValue(value)
        q.addBindValue(datos[0])
        if not q.exec():
            self.ui.lineEdit_txt.setText(
                f"Fallo actualizar_data(): {q.lastError().text()}"
            )

    def remover_data(self, item: int) -> None:
        sql = f"DELETE FROM Reserv_Clientes WHERE id = {item}"
        q = QSqlQuery()
        q.exec(sql)


    def buscar_Reserv(self):
        w = _Buscar()
        w.setGridParent(self)
        w.show()
        if w.exec() == _Buscar.Accepted:
            #_Buscar Database
            print("_Buscar Database Cerrado")


##  Preparar Base de Datos
    def Obtener_ID2(self):
        q = QSqlQuery()
        sql = "SELECT id FROM productos ORDER BY id DESC"
        q.exec(sql)

        if q.next():
            self.ID2 = q.value(0)
        else:
            self.ID2 = 0

        self.ui.lineEdit_txt.setText("ID2: "+str(self.ID2))

    def getNew_ID2(self):
        self.ID2 = str(int(self.ID2)+1)
        return self.ID2

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

    def Insertar(self):
        datos = (self.getNew_ID2(), self.ui.codigo_txt.text(), self.ui.nombre_txt.text(), self.ui.modelo_txt.text())
        self.NewRow_Table_Widget2(datos)
        self.insertar_producto(*datos[1:])


    def Modifi_rsv(self, row, col):
        self.row_tmp = row# Extraer Nro de fila
        datos = []
        for j in range(self.columnCount2()):
            item = self.ui.tableWidget_2.item(row, j)
            datos.append(item.text() if item else "")# Extraer datos
        
        (print("ID:", datos[0]), 
            self.ui.codigo_txt.setText(datos[1]),# Reasignar datos
            self.ui.nombre_txt.setText(datos[2]), 
            self.ui.modelo_txt.setText(datos[3]))

        #self.actualiza_productos()


    def Modifi_Base(self):
        if self.row_tmp is None:
            return

        datos = (None, self.ui.codigo_txt.text(), self.ui.nombre_txt.text(), self.ui.modelo_txt.text())
        for j in range(1, self.columnCount2()):
            item = self.ui.tableWidget_2.item(self.row_tmp, j)
            item.setText(str(datos[j])) ## 'id' y 'cod_clie' son 'int'
            self.ui.tableWidget_2.setItem(self.row_tmp, j, item)

        self.Update_data(datos[1],   datos[3],    datos[2],    self.ui.tableWidget_2.item(self.row_tmp, 0).text())
        self.row_tmp = None


    def Erase_Base(self):
        if self.row_tmp:
            item = self.ui.tableWidget_2.item(self.row_tmp, 0)#ID
            sql = "DELETE FROM productos WHERE id = {}".format(item.text())
            q = QSqlQuery()
            q.exec(sql)
            self.ui.tableWidget_2.removeRow(self.row_tmp)
            self.row_tmp = None


    def insertar_producto(self, codigo, nombre, modelo):
        sql = """INSERT INTO productos (CODIGO, NOMBRE, MODELO)
            VALUES(?, ?, ?)"""

        q = QSqlQuery()
        if q.prepare(sql):
            q.addBindValue(codigo)
            q.addBindValue(nombre)
            q.addBindValue(modelo)
            if q.exec():
                print("Campo agregado satisfactoriamente!")


    def Update_data(self, codigo, modelo,  nombre_producto, id):
        global db
        q = QSqlQuery()
        sql = """UPDATE productos
            SET CODIGO = ?, MODELO = ?, NOMBRE = ?
            WHERE id = ?"""
        if not q.prepare(sql):
            self.ui.lineEdit_txt.setText(
                f"Fallo Update_data(): {q.lastError().text()}"
            )
            return
        for value in (codigo, modelo, nombre_producto, id):
            q.addBindValue(value)
        if not q.exec():
            self.ui.lineEdit_txt.setText(
                f"Fallo Update_data(): {q.lastError().text()}"
            )
            return
        db.commit()



def prepareDataBase():
    global db
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("data.db")

    if db.open():
        q = QSqlQuery()
        q.exec("create table if not exists  Clientes (Cod_clie INTEGER primary key autoincrement not null, nombre TEXT not null, fecha TEXT not null)")
        print("TABLA  <Clientes>  creada satisfactoriamente!")

        q = QSqlQuery()
        q.exec("INSERT into Clientes VALUES(1, 'Maria', '8/11/2026')")
            
        q = QSqlQuery()
        q.exec("INSERT into Clientes VALUES(2, 'Juana', '7/11/2026')")
            
        q = QSqlQuery()
        q.exec("INSERT into Clientes VALUES(3, 'Matias', '5/11/2026')")
            
        q = QSqlQuery()
        q.exec("INSERT into Clientes VALUES(4, 'Esteban', '9/11/2026')")

        q = QSqlQuery()
        if q.prepare("create table if not exists  Reserv_Clientes (id integer primary key autoincrement not null, NOMBRE text not null, Cod_clie integer, fecha text not null, Trabajos text not null, precio text not null , Observaciones text not null )"):
            if q.exec():
                print("TABLA  <Reserv_Clientes>  creada satisfactoriamente!")
        db_create()

        q = QSqlQuery()
        if q.prepare("create table if not exists  Reserv_data (id integer primary key autoincrement not null, Cod_clie integer, fecha text not null, path text not null )"):
            if q.exec():
                print("TABLA  <Reserv_data>  creada satisfactoriamente!")

        q = QSqlQuery()
        if q.prepare("create table if not exists  productos (id integer primary key autoincrement not null, CODIGO text not null, NOMBRE text not null, MODELO text not null )"):
            if q.exec():
                print("TABLA  <productos>  creada satisfactoriamente!")

        Registro_db_create()

def db_create():
    query = QSqlQuery()
    ## prepareDataBase()
    query.exec("insert into productos values(101, 'Cod13', 'viernes', '11')")
    query.exec("insert into productos values(102, 'Cod13', 'viernes', '11')")
    query.exec("insert into productos values(103, 'fir12', 'sara', '77')")
    query.exec("insert into productos values(104, 'ir13', 'Sonia', '404')")


def Registro_db_create():
    query = QSqlQuery()
    query.exec("insert into Reserv_data values(111, '1', '5/04/2024' , 'C:/Users/FernandezMiguelA/Downloads/Gestor_remake/Imagenes/img_1.png')")
    query.exec("insert into Reserv_data values(112, '2', '10/04/2024', 'C:/Users/FernandezMiguelA/Downloads/Gestor_remake/Imagenes/img_2.png')")
    query.exec("insert into Reserv_data values(113, '3', '12/04/2024', 'C:/Users/FernandezMiguelA/Downloads/Gestor_remake/Imagenes/img_3.png')")


##

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    prepareDataBase()
    w = GUI()
    w.show()
    sys.exit(app.exec())