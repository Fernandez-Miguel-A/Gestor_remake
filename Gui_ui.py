# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 294)
        self.nuevo_btn = QPushButton(Form)
        self.nuevo_btn.setObjectName(u"nuevo_btn")
        self.nuevo_btn.setGeometry(QRect(70, 260, 75, 23))
        self.modif_btn = QPushButton(Form)
        self.modif_btn.setObjectName(u"modif_btn")
        self.modif_btn.setGeometry(QRect(150, 260, 75, 23))
        self.elim_btn = QPushButton(Form)
        self.elim_btn.setObjectName(u"elim_btn")
        self.elim_btn.setGeometry(QRect(230, 260, 75, 23))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 20, 751, 211))
        self.tableWidget.setAlternatingRowColors(True)
        self.busca_btn = QPushButton(Form)
        self.busca_btn.setObjectName(u"busca_btn")
        self.busca_btn.setGeometry(QRect(350, 260, 75, 23))
        self.lineEdit_txt = QLineEdit(Form)
        self.lineEdit_txt.setObjectName(u"lineEdit_txt")
        self.lineEdit_txt.setGeometry(QRect(450, 260, 113, 20))

        self.retranslateUi(Form)
        self.tableWidget.cellDoubleClicked.connect(self.modif_btn.toggle)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nuevo_btn.setText(QCoreApplication.translate("Form", u"Nuevo", None))
        self.modif_btn.setText(QCoreApplication.translate("Form", u"Modif", None))
        self.elim_btn.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Cod_clie", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"fecha", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Trabajos", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Precio", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Observaciones", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Cliente1", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Cliente2", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Cliente3", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Cliente4", None));
        self.busca_btn.setText(QCoreApplication.translate("Form", u"Buscar", None))
    # retranslateUi

