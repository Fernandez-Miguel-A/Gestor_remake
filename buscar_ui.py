# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buscar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Buscar_widget(object):
    def setupUi(self, Buscar_widget):
        if not Buscar_widget.objectName():
            Buscar_widget.setObjectName(u"Buscar_widget")
        Buscar_widget.resize(782, 312)
        self.gridLayout = QGridLayout(Buscar_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buscar_txt = QLineEdit(Buscar_widget)
        self.buscar_txt.setObjectName(u"buscar_txt")
        self.buscar_txt.setStyleSheet(u"background-color: rgb(255, 71, 71);")

        self.gridLayout.addWidget(self.buscar_txt, 0, 2, 1, 1)

        self.buscar_btn = QPushButton(Buscar_widget)
        self.buscar_btn.setObjectName(u"buscar_btn")

        self.gridLayout.addWidget(self.buscar_btn, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(Buscar_widget)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.tipodecelda_cmb = QComboBox(Buscar_widget)
        self.tipodecelda_cmb.addItem("")
        self.tipodecelda_cmb.addItem("")
        self.tipodecelda_cmb.addItem("")
        self.tipodecelda_cmb.addItem("")
        self.tipodecelda_cmb.addItem("")
        self.tipodecelda_cmb.addItem("")
        self.tipodecelda_cmb.addItem("")
        self.tipodecelda_cmb.setObjectName(u"tipodecelda_cmb")
        self.tipodecelda_cmb.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.tipodecelda_cmb, 0, 1, 1, 1)


        self.retranslateUi(Buscar_widget)

        QMetaObject.connectSlotsByName(Buscar_widget)
    # setupUi

    def retranslateUi(self, Buscar_widget):
        Buscar_widget.setWindowTitle(QCoreApplication.translate("Buscar_widget", u"Form", None))
        self.buscar_btn.setText(QCoreApplication.translate("Buscar_widget", u"buscar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Buscar_widget", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Buscar_widget", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Buscar_widget", u"Cod_clie", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Buscar_widget", u"fecha", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Buscar_widget", u"Trabajos", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Buscar_widget", u"Precio", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Buscar_widget", u"Observaciones", None));
        self.tipodecelda_cmb.setItemText(0, QCoreApplication.translate("Buscar_widget", u"ID", None))
        self.tipodecelda_cmb.setItemText(1, QCoreApplication.translate("Buscar_widget", u"Nombre", None))
        self.tipodecelda_cmb.setItemText(2, QCoreApplication.translate("Buscar_widget", u"Cod_clie", None))
        self.tipodecelda_cmb.setItemText(3, QCoreApplication.translate("Buscar_widget", u"fecha", None))
        self.tipodecelda_cmb.setItemText(4, QCoreApplication.translate("Buscar_widget", u"Trabajos", None))
        self.tipodecelda_cmb.setItemText(5, QCoreApplication.translate("Buscar_widget", u"Precio", None))
        self.tipodecelda_cmb.setItemText(6, QCoreApplication.translate("Buscar_widget", u"Observaciones", None))

    # retranslateUi

