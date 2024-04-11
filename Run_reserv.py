#Run_reserv.py

import re

from reserv_ui import Ui_Dialog



from PySide2.QtWidgets import QDialog, QApplication, QDateTimeEdit
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt, QDateTime

from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel


# class ClassName(Ui_Dialog, QDialog):
#     """docstring for ClassName"""
#     def __init__(self):
#         super(ClassName, self).__init__()
#         super(ClassName, self).setupUi(self)
#         self.arg = None



class Reserv(QDialog):
    """docstring for Reserv"""
    def __init__(self, data= None):
        super(Reserv, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.arg =  data if data else (None, "Maria", "3", "7/04/2024", "DEGRADE                                     $3000", "$3000", "")
        #self.arg = (None, "Maria", "3", "7/04/2024", "DEGRADE", "$3000", "")
        self.arg2_tipe = 0

        if self.arg2_tipe == 0:
            self.ui.ok_btn.setText("Ok")#Nuevo
        elif self.arg2_tipe == 1:
            self.ui.ok_btn.setText("Modif")#Modificar
        else:
            self.ui.ok_btn.setText("Borrar")#Eliminar

        ##self.ui.trab_listW.clicked.connect(lambda x: self.function("adsdas"))
        #self.ui.trab_listW.itemClicked.connect(self.trabajos_act)
        self.ui.trab_listW.itemDoubleClicked.connect(self.trabajos_act)
        self.ui.trab_listW.itemChanged.connect(self.Precios)#itemChanged, itemActivated

        self.loadData()
        self.Precios()

    def loadData(self):
        self.ui.id_l.setText(":"+str(self.arg[0])+":")# campo ID
        self.ui.name_txt.setText(self.arg[1])## ok + str(self.arg[0])
        self.ui.precio_txt.setText(self.arg[5])
        self.ui.obs_txt.setText(self.arg[6])

        for o in self.arg[4].split("|"):
            trbs = self.ui.trab_listW.findItems(o, Qt.MatchExactly)
            if trbs:
                trb = trbs[0]
                trb.setCheckState(Qt.Checked)


        if self.arg[2]:
            if self.arg[2] != "0":##Ico_l
                self.ui.N_Clie_cmb.insertItem(self.ui.N_Clie_cmb.count(), self.arg[2])
                self.ui.N_Clie_cmb.setCurrentText(self.arg[2])

                self.load_Ico(self.arg[2])
                self.ui.N_Clie_cmb.currentTextChanged.connect(self.load_Ico)


        datetime = QDateTime.fromString(self.arg[3], "d/M/yyyy")
        ##self.ui.obs_txt.setText(str(datetime))##mostrar el datetime cargado en crudo
        self.ui.work_date.setDateTime(datetime)

    def load_Ico(self, cod_clie):
        ##cod_clie == self.arg[2]
        print("load_Ico(cod_clie):", cod_clie)
        if cod_clie == "0":
            self.ui.Ico_l.setPixmap(None)
            #self.ui.reg_date.setDateTime(None)
            return
        q = QSqlQuery()
        sql = "SELECT path, fecha FROM Reserv_data WHERE Cod_clie = '%s' "%(cod_clie)### self.ui.N_Clie_cmb.currentIndex()
        q.exec_(sql)
        if q.next():
            path = q.value(0)
            fecha = q.value(1)

            pix = QPixmap(path)
            self.ui.Ico_l.setPixmap(pix.scaled(120, 100))

            # datetime = QDateTime.fromString(fecha, "d/M/yyyy")
            # self.ui.reg_date.setDateTime(datetime)

        else:
            self.ui.Ico_l.setPixmap(None)
            #self.ui.reg_date.setDateTime(None)
            return



    def function(self, name_item):#añade un nuevo ListWIdem
        print(name_item)
        self.ui.trab_listW.addItem(name_item)   #Nuevo ListWidgetItem
        #self.ui.name_txt.setText(name_item)

        trb = self.ui.trab_listW.item(self.ui.trab_listW.count()-1)
        trb.setCheckState(Qt.Unchecked)

    def trabajos_act(self, trb):
        ##self.function("adsaasd")
        #self.ui.name_txt.setText(trb.text())
        
        if trb.checkState() == Qt.Checked:
            trb.setCheckState(Qt.Unchecked)
        else:
            trb.setCheckState(Qt.Checked)

        #self.Precios()

    def Precios(self, item=None):
        precio_final = 0
        #self.ui.obs_txt.setText("$"+str(precio_final))
        #elf.ui.name_txt.setText(self.ui.trab_listW.item(0).text())
        for i in range(self.ui.trab_listW.count()):
            trb = self.ui.trab_listW.item(i)
            #self.ui.name_txt.setText(trb.text())
            #self.ui.name_txt.setText(str(i))

            if trb.checkState() == Qt.Checked:
                #self.ui.obs_txt.setText(str(precio_final))
                precio = re.findall(r"\$(\d+)", trb.text())
                if not precio:
                    continue
                else:
                    precio = precio[0]
                precio_final += int(precio)
        self.ui.precio_txt.setText("$"+str(precio_final))

    def trabajos(self):
        _trabajos = ""
        for i in range(self.ui.trab_listW.count()):
            trb = self.ui.trab_listW.item(i)
            if trb.checkState() == Qt.Checked:
                _trabajos += "|" + trb.text()
        _trabajos = _trabajos[1:] if _trabajos else ""
        return _trabajos

    def get_data(self):
        datos = [self.arg[0], ## if datos[0] is "":;   datos[0] = self.getNew_ID()
            self.ui.name_txt.text(), self.ui.N_Clie_cmb.currentText(), self.ui.work_date.date().toString("d/M/yyyy"),
            self.trabajos(), self.ui.precio_txt.text(), self.ui.obs_txt.toPlainText()]#nombre_txt, falta trabajar en 'date()'

        print("Los datos son: ", datos)
        return datos




if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    w = Reserv()
    w.show()
    sys.exit(app.exec_())