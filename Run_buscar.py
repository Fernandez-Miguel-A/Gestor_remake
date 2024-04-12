#Run_reserv.py

import re

from buscar_ui import Ui_Buscar_widget



from PySide2.QtWidgets import QDialog, QApplication, QDateTimeEdit, QWidget, QTableWidgetItem
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt, QDateTime

from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

#remix copado   puro clasicos
#https://www.youtube.com/watch?v=WRGySfs4Pqc


###background-color: rgb(71, 255, 71);background-color: rgb(255, 71, 71);
class _Buscar(QDialog):
    """docstring for _Buscar"""
    def __init__(self):
        super(_Buscar, self).__init__()
        self.ui = Ui_Buscar_widget()
        self.ui.setupUi(self)
        self.ui.buscar_txt.setStyleSheet(u"background-color: rgb(255, 71, 71);")

        self.ui.buscar_btn.clicked.connect(self.buscar)

    def buscar(self):
        print("\n\nbuscar: ", self.ui.tipodecelda_cmb.currentText(), self.ui.buscar_txt.text())
        self.clearTable()
        query = QSqlQuery()
        sql = "select * FROM Reserv_Clientes WHERE Cod_clie = '{}'".format(self.ui.buscar_txt.text())
        sql1 = "select * FROM Reserv_Clientes WHERE {} = '{}'".format(self.ui.tipodecelda_cmb.currentText(), self.ui.buscar_txt.text())
        sql2 = "select id, {} FROM Reserv_Clientes WHERE id > 0".format(self.ui.tipodecelda_cmb.currentText())
        
        print("sql", sql2)
        query.exec_(sql2)
        # while q.next():
        #     datos = [q.value(i) for i in range(self.columnCount())]
        #     self.NewRow_Table_Widget(datos)

        i = 0
        self.ui.buscar_txt.setStyleSheet(u"background-color: rgb(255, 71, 71);")
        if not self.ui.buscar_txt.text().upper():
            return
        while query.next():
            id = query.value(0)
            campo_var = str(query.value(1))
            ##find = re.findall("(.*"+self.ui.buscar_txt.text()+".*)", campo_var)
            reg_exp = re.compile("(.*"+self.ui.buscar_txt.text().upper()+".*)", re.IGNORECASE)
            find = reg_exp.findall(campo_var)
            print("\n\nCeldas", i)
            i += 1
            print("find", find, reg_exp, self.ui.buscar_txt.text().upper())
            print("id, campo_var", id, campo_var)
            if find:
                q = QSqlQuery()
                sql = "select * FROM Reserv_Clientes WHERE id = {}".format(id)
                q.exec_(sql)
                while q.next():
                    datos = [q.value(i) for i in range(self.columnCount())]
                    self.NewRow_Table_Widget(datos)

                self.ui.buscar_txt.setStyleSheet(u"background-color: rgb(71, 255, 71);")
            # else:
            #     self.ui.buscar_txt.setStyleSheet(u"background-color: rgb(255, 71, 71);")
        


    def clearTable(self):
        rows = self.rowCount()
        [self.ui.tableWidget.removeRow(0) for row in range(rows)]



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


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    w = _Buscar()
    w.show()
    sys.exit(app.exec_())