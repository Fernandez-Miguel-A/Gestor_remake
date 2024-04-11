#Run_reserv.py

import re

from buscar_ui import Ui_Buscar_widget



from PySide2.QtWidgets import QDialog, QApplication, QDateTimeEdit
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt, QDateTime

from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

#remix copado   puro clasicos
#https://www.youtube.com/watch?v=WRGySfs4Pqc


###background-color: rgb(0, 255, 0);background-color: rgb(255, 0, 0);
class _Buscar(QDialog):
    """docstring for _Buscar"""
    def __init__(self):
        super(_Buscar, self).__init__()
        self.ui = Ui_Buscar_widget()
        self.ui.setupUi(self)
        self.buscar_btn.setStyleSheet(u"background-color: rgb(255, 0, 0);")




if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    w = _Buscar()
    w.show()
    sys.exit(app.exec_())