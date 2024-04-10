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
        Form.resize(817, 310)
        self.nuevo_btn = QPushButton(Form)
        self.nuevo_btn.setObjectName(u"nuevo_btn")
        self.nuevo_btn.setGeometry(QRect(70, 280, 75, 23))
        self.modif_btn = QPushButton(Form)
        self.modif_btn.setObjectName(u"modif_btn")
        self.modif_btn.setGeometry(QRect(150, 280, 75, 23))
        self.elim_btn = QPushButton(Form)
        self.elim_btn.setObjectName(u"elim_btn")
        self.elim_btn.setGeometry(QRect(230, 280, 75, 23))
        self.busca_btn = QPushButton(Form)
        self.busca_btn.setObjectName(u"busca_btn")
        self.busca_btn.setGeometry(QRect(350, 280, 75, 23))
        self.lineEdit_txt = QLineEdit(Form)
        self.lineEdit_txt.setObjectName(u"lineEdit_txt")
        self.lineEdit_txt.setGeometry(QRect(450, 280, 113, 20))
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 771, 251))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableWidget = QTableWidget(self.tab)
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
        self.tableWidget.setGeometry(QRect(0, 0, 751, 211))
        self.tableWidget.setAlternatingRowColors(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(40, 10, 411, 192))
        self.new_btn = QPushButton(self.tab_2)
        self.new_btn.setObjectName(u"new_btn")
        self.new_btn.setGeometry(QRect(490, 70, 75, 23))
        self.modif_btn_2 = QPushButton(self.tab_2)
        self.modif_btn_2.setObjectName(u"modif_btn_2")
        self.modif_btn_2.setGeometry(QRect(490, 100, 75, 23))
        self.codigo_txt = QLineEdit(self.tab_2)
        self.codigo_txt.setObjectName(u"codigo_txt")
        self.codigo_txt.setGeometry(QRect(640, 10, 113, 20))
        self.nombre_txt = QLineEdit(self.tab_2)
        self.nombre_txt.setObjectName(u"nombre_txt")
        self.nombre_txt.setGeometry(QRect(640, 60, 113, 20))
        self.modelo_txt = QLineEdit(self.tab_2)
        self.modelo_txt.setObjectName(u"modelo_txt")
        self.modelo_txt.setGeometry(QRect(640, 120, 113, 20))
        self.codigo_l = QLabel(self.tab_2)
        self.codigo_l.setObjectName(u"codigo_l")
        self.codigo_l.setGeometry(QRect(580, 20, 47, 13))
        self.nombre_l = QLabel(self.tab_2)
        self.nombre_l.setObjectName(u"nombre_l")
        self.nombre_l.setGeometry(QRect(580, 60, 47, 13))
        self.modelo_l = QLabel(self.tab_2)
        self.modelo_l.setObjectName(u"modelo_l")
        self.modelo_l.setGeometry(QRect(580, 120, 47, 13))
        self.elim_btn_2 = QPushButton(self.tab_2)
        self.elim_btn_2.setObjectName(u"elim_btn_2")
        self.elim_btn_2.setGeometry(QRect(490, 130, 75, 23))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tableWidget.cellDoubleClicked.connect(self.modif_btn.toggle)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nuevo_btn.setText(QCoreApplication.translate("Form", u"Nuevo", None))
        self.modif_btn.setText(QCoreApplication.translate("Form", u"Modif", None))
        self.elim_btn.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.busca_btn.setText(QCoreApplication.translate("Form", u"Buscar", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Tab 1", None))
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Codigo", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Modelo", None));
        self.new_btn.setText(QCoreApplication.translate("Form", u"New", None))
        self.modif_btn_2.setText(QCoreApplication.translate("Form", u"Modif", None))
        self.codigo_l.setText(QCoreApplication.translate("Form", u"Codigo", None))
        self.nombre_l.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.modelo_l.setText(QCoreApplication.translate("Form", u"Modelo", None))
        self.elim_btn_2.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi

