# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Reserv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 432)
        self.ok_btn = QPushButton(Dialog)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(300, 376, 75, 23))
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-3, 403, 461, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.color_fr = QFrame(Dialog)
        self.color_fr.setObjectName(u"color_fr")
        self.color_fr.setGeometry(QRect(0, 0, 461, 411))
        self.color_fr.setStyleSheet(u"background-color: rgb(106, 255, 98);")
        self.color_fr.setFrameShape(QFrame.StyledPanel)
        self.color_fr.setFrameShadow(QFrame.Raised)
        self.N_Clie_cmb = QComboBox(Dialog)
        self.N_Clie_cmb.addItem("")
        self.N_Clie_cmb.setObjectName(u"N_Clie_cmb")
        self.N_Clie_cmb.setGeometry(QRect(61, 50, 69, 22))
        self.Ico = QLabel(Dialog)
        self.Ico.setObjectName(u"Ico")
        self.Ico.setGeometry(QRect(330, 20, 121, 101))
        self.Ico.setStyleSheet(u"background-color: rgb(255, 123, 242);")
        self.Ico.setAlignment(Qt.AlignCenter)
        self.name_txt = QLineEdit(Dialog)
        self.name_txt.setObjectName(u"name_txt")
        self.name_txt.setGeometry(QRect(60, 20, 171, 20))
        self.name_l = QLabel(Dialog)
        self.name_l.setObjectName(u"name_l")
        self.name_l.setGeometry(QRect(9, 24, 47, 13))
        self.cod_clie_l = QLabel(Dialog)
        self.cod_clie_l.setObjectName(u"cod_clie_l")
        self.cod_clie_l.setGeometry(QRect(10, 54, 47, 13))
        self.obs_txt = QTextEdit(Dialog)
        self.obs_txt.setObjectName(u"obs_txt")
        self.obs_txt.setGeometry(QRect(10, 190, 361, 181))
        self.Obs_l = QLabel(Dialog)
        self.Obs_l.setObjectName(u"Obs_l")
        self.Obs_l.setGeometry(QRect(10, 168, 81, 16))
        self.Trabajos_fr = QFrame(Dialog)
        self.Trabajos_fr.setObjectName(u"Trabajos_fr")
        self.Trabajos_fr.setGeometry(QRect(140, 120, 311, 201))
        self.Trabajos_fr.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.Trabajos_fr.setFrameShape(QFrame.Box)
        self.Trabajos_fr.setFrameShadow(QFrame.Sunken)
        self.trab_listW = QListWidget(self.Trabajos_fr)
        __qlistwidgetitem = QListWidgetItem(self.trab_listW)
        __qlistwidgetitem.setCheckState(Qt.Unchecked);
        __qlistwidgetitem1 = QListWidgetItem(self.trab_listW)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2 = QListWidgetItem(self.trab_listW)
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3 = QListWidgetItem(self.trab_listW)
        __qlistwidgetitem3.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4 = QListWidgetItem(self.trab_listW)
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        self.trab_listW.setObjectName(u"trab_listW")
        self.trab_listW.setGeometry(QRect(30, 10, 256, 161))
        self.line_2 = QFrame(self.Trabajos_fr)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(5, 164, 281, 16))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.precio_l = QLabel(self.Trabajos_fr)
        self.precio_l.setObjectName(u"precio_l")
        self.precio_l.setGeometry(QRect(150, 180, 47, 13))
        self.precio_txt = QLineEdit(self.Trabajos_fr)
        self.precio_txt.setObjectName(u"precio_txt")
        self.precio_txt.setGeometry(QRect(194, 178, 91, 20))
        self.precio_txt.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.precio_txt.setReadOnly(True)
        self.Trab_btn = QPushButton(Dialog)
        self.Trab_btn.setObjectName(u"Trab_btn")
        self.Trab_btn.setGeometry(QRect(10, 120, 75, 23))
        self.Trab_btn.setCheckable(True)
        self.Trab_btn.setChecked(True)
        self.fecha = QLabel(Dialog)
        self.fecha.setObjectName(u"fecha")
        self.fecha.setGeometry(QRect(9, 94, 47, 13))
        self.reg_nro_l = QLabel(Dialog)
        self.reg_nro_l.setObjectName(u"reg_nro_l")
        self.reg_nro_l.setGeometry(QRect(160, 50, 71, 20))
        self.reg_date = QDateEdit(Dialog)
        self.reg_date.setObjectName(u"reg_date")
        self.reg_date.setEnabled(False)
        self.reg_date.setGeometry(QRect(230, 50, 91, 20))
        self.reg_date.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.reg_date.setCalendarPopup(True)
        self.cancel_btn = QPushButton(Dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(382, 376, 75, 23))
        self.work_date = QDateEdit(Dialog)
        self.work_date.setObjectName(u"work_date")
        self.work_date.setEnabled(True)
        self.work_date.setGeometry(QRect(60, 90, 91, 20))
        self.work_date.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.work_date.setCalendarPopup(True)
        self.id_l = QLabel(Dialog)
        self.id_l.setObjectName(u"id_l")
        self.id_l.setGeometry(QRect(239, 22, 21, 16))
        self.color_fr.raise_()
        self.obs_txt.raise_()
        self.line.raise_()
        self.N_Clie_cmb.raise_()
        self.Ico.raise_()
        self.name_txt.raise_()
        self.name_l.raise_()
        self.cod_clie_l.raise_()
        self.Obs_l.raise_()
        self.ok_btn.raise_()
        self.Trabajos_fr.raise_()
        self.Trab_btn.raise_()
        self.fecha.raise_()
        self.reg_nro_l.raise_()
        self.reg_date.raise_()
        self.cancel_btn.raise_()
        self.work_date.raise_()
        self.id_l.raise_()
        QWidget.setTabOrder(self.ok_btn, self.name_txt)
        QWidget.setTabOrder(self.name_txt, self.N_Clie_cmb)
        QWidget.setTabOrder(self.N_Clie_cmb, self.reg_date)
        QWidget.setTabOrder(self.reg_date, self.Trab_btn)
        QWidget.setTabOrder(self.Trab_btn, self.trab_listW)
        QWidget.setTabOrder(self.trab_listW, self.precio_txt)
        QWidget.setTabOrder(self.precio_txt, self.obs_txt)

        self.retranslateUi(Dialog)
        self.N_Clie_cmb.currentIndexChanged.connect(self.reg_date.show)
        self.cancel_btn.clicked.connect(Dialog.reject)
        self.ok_btn.clicked.connect(Dialog.accept)
        self.Trab_btn.toggled.connect(self.Trabajos_fr.setVisible)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.ok_btn.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.N_Clie_cmb.setItemText(0, QCoreApplication.translate("Dialog", u"0", None))

        self.Ico.setText(QCoreApplication.translate("Dialog", u"img_Ico", None))
        self.name_l.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.cod_clie_l.setText(QCoreApplication.translate("Dialog", u"Cod_clie", None))
        self.obs_txt.setPlaceholderText(QCoreApplication.translate("Dialog", u"Prefer cut, wosh", None))
        self.Obs_l.setText(QCoreApplication.translate("Dialog", u"Observaciones:", None))

        __sortingEnabled = self.trab_listW.isSortingEnabled()
        self.trab_listW.setSortingEnabled(False)
        ___qlistwidgetitem = self.trab_listW.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"DEGRADE                                     $3000", None));
        ___qlistwidgetitem1 = self.trab_listW.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"Nuevo elemento                         $0", None));
        ___qlistwidgetitem2 = self.trab_listW.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"PINTURA                                        $4000", None));
        ___qlistwidgetitem3 = self.trab_listW.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"AFEITADO                                      $800", None));
        ___qlistwidgetitem4 = self.trab_listW.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"Corte_de_Pelo                              $3000", None));
        self.trab_listW.setSortingEnabled(__sortingEnabled)

        self.precio_l.setText(QCoreApplication.translate("Dialog", u"Precio:", None))
        self.precio_txt.setText(QCoreApplication.translate("Dialog", u"$ 0", None))
        self.Trab_btn.setText(QCoreApplication.translate("Dialog", u"Trabajos", None))
        self.fecha.setText(QCoreApplication.translate("Dialog", u"fecha", None))
        self.reg_nro_l.setText(QCoreApplication.translate("Dialog", u"Registro nro:", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.id_l.setText(QCoreApplication.translate("Dialog", u"1", None))
    # retranslateUi

