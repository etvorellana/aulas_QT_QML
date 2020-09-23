# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario_00PHAHIy.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Formulario(object):
    def setupUi(self, Formulario):
        if not Formulario.objectName():
            Formulario.setObjectName(u"Formulario")
        Formulario.resize(456, 200)
        Formulario.setMinimumSize(QSize(300, 200))
        self.horizontalLayout_3 = QHBoxLayout(Formulario)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_lbl = QLabel(Formulario)
        self.info_lbl.setObjectName(u"info_lbl")

        self.verticalLayout.addWidget(self.info_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.alm1_cbx = QComboBox(Formulario)
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.addItem("")
        self.alm1_cbx.setObjectName(u"alm1_cbx")

        self.horizontalLayout.addWidget(self.alm1_cbx)

        self.pre1R_sbx = QSpinBox(Formulario)
        self.pre1R_sbx.setObjectName(u"pre1R_sbx")
        self.pre1R_sbx.setMaximum(100)
        self.pre1R_sbx.setValue(0)

        self.horizontalLayout.addWidget(self.pre1R_sbx)

        self.pre1C_sbx = QSpinBox(Formulario)
        self.pre1C_sbx.setObjectName(u"pre1C_sbx")

        self.horizontalLayout.addWidget(self.pre1C_sbx)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.alm2_cbx = QComboBox(Formulario)
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.addItem("")
        self.alm2_cbx.setObjectName(u"alm2_cbx")

        self.horizontalLayout_2.addWidget(self.alm2_cbx)

        self.pre2R_sbx = QSpinBox(Formulario)
        self.pre2R_sbx.setObjectName(u"pre2R_sbx")
        self.pre2R_sbx.setMaximum(100)

        self.horizontalLayout_2.addWidget(self.pre2R_sbx)

        self.pre2C_sbx = QSpinBox(Formulario)
        self.pre2C_sbx.setObjectName(u"pre2C_sbx")

        self.horizontalLayout_2.addWidget(self.pre2C_sbx)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.total_lbl = QLabel(Formulario)
        self.total_lbl.setObjectName(u"total_lbl")
        self.total_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.total_lbl)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Formulario)

        QMetaObject.connectSlotsByName(Formulario)
    # setupUi

    def retranslateUi(self, Formulario):
        Formulario.setWindowTitle(QCoreApplication.translate("Formulario", u"Formulario", None))
        self.info_lbl.setText(QCoreApplication.translate("Formulario", u"Selecione 2 itens que voc\u00ea almo\u00e7ou e seus pre\u00e7os.", None))
        self.alm1_cbx.setItemText(0, QCoreApplication.translate("Formulario", u"ovos", None))
        self.alm1_cbx.setItemText(1, QCoreApplication.translate("Formulario", u"misto quente", None))
        self.alm1_cbx.setItemText(2, QCoreApplication.translate("Formulario", u"queijo quente", None))
        self.alm1_cbx.setItemText(3, QCoreApplication.translate("Formulario", u"queijo", None))
        self.alm1_cbx.setItemText(4, QCoreApplication.translate("Formulario", u"homus", None))
        self.alm1_cbx.setItemText(5, QCoreApplication.translate("Formulario", u"iogurte", None))
        self.alm1_cbx.setItemText(6, QCoreApplication.translate("Formulario", u"ma\u00e7\u00e3", None))
        self.alm1_cbx.setItemText(7, QCoreApplication.translate("Formulario", u"banana", None))
        self.alm1_cbx.setItemText(8, QCoreApplication.translate("Formulario", u"laranja", None))
        self.alm1_cbx.setItemText(9, QCoreApplication.translate("Formulario", u"p\u00e3o de quijo", None))
        self.alm1_cbx.setItemText(10, QCoreApplication.translate("Formulario", u"cenouras", None))
        self.alm1_cbx.setItemText(11, QCoreApplication.translate("Formulario", u"p\u00e3o", None))
        self.alm1_cbx.setItemText(12, QCoreApplication.translate("Formulario", u"macarr\u00e3o", None))
        self.alm1_cbx.setItemText(13, QCoreApplication.translate("Formulario", u"tapioca", None))
        self.alm1_cbx.setItemText(14, QCoreApplication.translate("Formulario", u"batatas fritas", None))
        self.alm1_cbx.setItemText(15, QCoreApplication.translate("Formulario", u"caf\u00e9", None))
        self.alm1_cbx.setItemText(16, QCoreApplication.translate("Formulario", u"refrigerante", None))
        self.alm1_cbx.setItemText(17, QCoreApplication.translate("Formulario", u"\u00e1gua", None))
        self.alm1_cbx.setItemText(18, QCoreApplication.translate("Formulario", u"Caf\u00e9 com Leite", None))

        self.pre1R_sbx.setSpecialValueText("")
        self.pre1R_sbx.setPrefix(QCoreApplication.translate("Formulario", u"R$", None))
        self.pre1C_sbx.setPrefix(QCoreApplication.translate("Formulario", u".", None))
        self.alm2_cbx.setItemText(0, QCoreApplication.translate("Formulario", u"ovos", None))
        self.alm2_cbx.setItemText(1, QCoreApplication.translate("Formulario", u"misto quente", None))
        self.alm2_cbx.setItemText(2, QCoreApplication.translate("Formulario", u"queijo quente", None))
        self.alm2_cbx.setItemText(3, QCoreApplication.translate("Formulario", u"queijo", None))
        self.alm2_cbx.setItemText(4, QCoreApplication.translate("Formulario", u"homus", None))
        self.alm2_cbx.setItemText(5, QCoreApplication.translate("Formulario", u"iogurte", None))
        self.alm2_cbx.setItemText(6, QCoreApplication.translate("Formulario", u"ma\u00e7\u00e3", None))
        self.alm2_cbx.setItemText(7, QCoreApplication.translate("Formulario", u"banana", None))
        self.alm2_cbx.setItemText(8, QCoreApplication.translate("Formulario", u"laranja", None))
        self.alm2_cbx.setItemText(9, QCoreApplication.translate("Formulario", u"p\u00e3o de quijo", None))
        self.alm2_cbx.setItemText(10, QCoreApplication.translate("Formulario", u"cenouras", None))
        self.alm2_cbx.setItemText(11, QCoreApplication.translate("Formulario", u"p\u00e3o", None))
        self.alm2_cbx.setItemText(12, QCoreApplication.translate("Formulario", u"macarr\u00e3o", None))
        self.alm2_cbx.setItemText(13, QCoreApplication.translate("Formulario", u"tapioca", None))
        self.alm2_cbx.setItemText(14, QCoreApplication.translate("Formulario", u"batatas fritas", None))
        self.alm2_cbx.setItemText(15, QCoreApplication.translate("Formulario", u"caf\u00e9", None))
        self.alm2_cbx.setItemText(16, QCoreApplication.translate("Formulario", u"refrigerante", None))
        self.alm2_cbx.setItemText(17, QCoreApplication.translate("Formulario", u"\u00e1gua", None))

        self.pre2R_sbx.setPrefix(QCoreApplication.translate("Formulario", u"R$", None))
        self.pre2C_sbx.setPrefix(QCoreApplication.translate("Formulario", u".", None))
        self.total_lbl.setText(QCoreApplication.translate("Formulario", u"Total: R$", None))
    # retranslateUi

