# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

from pyDrillDown.libs.view import GView

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(817, 309)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(200, 150))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setAlternatingRowColors(True)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
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

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nuevo_btn = QPushButton(Form)
        self.nuevo_btn.setObjectName(u"nuevo_btn")

        self.horizontalLayout.addWidget(self.nuevo_btn)

        self.modif_btn = QPushButton(Form)
        self.modif_btn.setObjectName(u"modif_btn")

        self.horizontalLayout.addWidget(self.modif_btn)

        self.elim_btn = QPushButton(Form)
        self.elim_btn.setObjectName(u"elim_btn")

        self.horizontalLayout.addWidget(self.elim_btn)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buscar_btn = QPushButton(Form)
        self.buscar_btn.setObjectName(u"buscar_btn")

        self.horizontalLayout.addWidget(self.buscar_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lineEdit_txt = QLineEdit(Form)
        self.lineEdit_txt.setObjectName(u"lineEdit_txt")

        self.horizontalLayout.addWidget(self.lineEdit_txt)

        self.chk_Todos = QCheckBox(Form)
        self.chk_Todos.setObjectName(u"chk_Todos")
        self.chk_Todos.setChecked(True)

        self.horizontalLayout.addWidget(self.chk_Todos)

        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setEnabled(False)
        self.dateEdit.setMinimumSize(QSize(90, 0))
        self.dateEdit.setDateTime(QDateTime(QDate(2024, 4, 8), QTime(13, 0, 0)))
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.dateEdit)

        self.View_Table = QCheckBox(Form)
        self.View_Table.setObjectName(u"View_Table")

        self.horizontalLayout.addWidget(self.View_Table)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.graphicsView = GView(Form)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Cod_clie", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"fecha", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Trabajos", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Precio", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Observaciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Tab 1", None))
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"ID", None))
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Codigo", None))
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Nombre", None))
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Modelo", None))
        self.new_btn.setText(QCoreApplication.translate("Form", u"New", None))
        self.modif_btn_2.setText(QCoreApplication.translate("Form", u"Modif", None))
        self.codigo_l.setText(QCoreApplication.translate("Form", u"Codigo", None))
        self.nombre_l.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.modelo_l.setText(QCoreApplication.translate("Form", u"Modelo", None))
        self.elim_btn_2.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
        self.nuevo_btn.setText(QCoreApplication.translate("Form", u"Nuevo", None))
        self.modif_btn.setText(QCoreApplication.translate("Form", u"Modif", None))
        self.elim_btn.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.buscar_btn.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.chk_Todos.setText(QCoreApplication.translate("Form", u"Todos", None))
        self.View_Table.setText(QCoreApplication.translate("Form", u"IconView", None))
    # retranslateUi

