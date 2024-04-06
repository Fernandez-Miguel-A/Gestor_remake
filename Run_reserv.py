#Run_reserv.py

import re

from reserv_ui import Ui_Dialog



from PySide2.QtWidgets import QDialog, QApplication
from PySide2.QtCore import Qt


# class ClassName(Ui_Dialog, QDialog):
#     """docstring for ClassName"""
#     def __init__(self):
#         super(ClassName, self).__init__()
#         super(ClassName, self).setupUi(self)
#         self.arg = None



class Reserv(QDialog):
    """docstring for Reserv"""
    def __init__(self):
        super(Reserv, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.arg = (None, "Maria", "3", "6/04/2024", "DEGRADE", "$3000", "")
        self.arg2_tipe = 0

        if self.arg2_tipe == 0:
            self.ui.ok_btn.setText("Ok")#Nuevo
        elif self.arg2_tipe == 1:
            self.ui.ok_btn.setText("Modif")#Modificar
        else:
            self.ui.ok_btn.setText("Ok")#Eliminar

        ##self.ui.trab_listW.clicked.connect(lambda x: self.function("adsdas"))
        #self.ui.trab_listW.itemClicked.connect(self.trabajos_act)
        self.ui.trab_listW.itemDoubleClicked.connect(self.trabajos_act)
        self.ui.trab_listW.itemChanged.connect(self.Precios)#itemChanged, itemActivated
        self.Precios()


    def function(self, name_item):
        print(name_item)
        self.ui.trab_listW.addItem(name_item)   #Nuevo ListWidgetItem
        #self.ui.name_txt.setText(name_item)

        trb = self.ui.trab_listW.item(self.ui.trab_listW.count()-1)
        trb.setCheckState(Qt.Unchecked)

    def trabajos_act(self, trb):
        self.function("adsaasd")
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




if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    w = Reserv()
    w.show()
    sys.exit(app.exec_())