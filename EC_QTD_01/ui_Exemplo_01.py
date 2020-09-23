# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Exemplo_01eRTFbr.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(410, 300)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.red_lbl = QLabel(Form)
        self.red_lbl.setObjectName(u"red_lbl")

        self.verticalLayout.addWidget(self.red_lbl)

        self.red_spb = QSpinBox(Form)
        self.red_spb.setObjectName(u"red_spb")
        self.red_spb.setMaximum(255)

        self.verticalLayout.addWidget(self.red_spb)

        self.red_vsl = QSlider(Form)
        self.red_vsl.setObjectName(u"red_vsl")
        self.red_vsl.setMaximum(255)
        self.red_vsl.setOrientation(Qt.Vertical)

        self.verticalLayout.addWidget(self.red_vsl)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.grn_lbl = QLabel(Form)
        self.grn_lbl.setObjectName(u"grn_lbl")

        self.verticalLayout_2.addWidget(self.grn_lbl)

        self.grn_spb = QSpinBox(Form)
        self.grn_spb.setObjectName(u"grn_spb")
        self.grn_spb.setMaximum(255)

        self.verticalLayout_2.addWidget(self.grn_spb)

        self.grn_vsl = QSlider(Form)
        self.grn_vsl.setObjectName(u"grn_vsl")
        self.grn_vsl.setMaximum(255)
        self.grn_vsl.setOrientation(Qt.Vertical)

        self.verticalLayout_2.addWidget(self.grn_vsl)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ble_lbl = QLabel(Form)
        self.ble_lbl.setObjectName(u"ble_lbl")

        self.verticalLayout_3.addWidget(self.ble_lbl)

        self.ble_spb = QSpinBox(Form)
        self.ble_spb.setObjectName(u"ble_spb")
        self.ble_spb.setMaximum(255)

        self.verticalLayout_3.addWidget(self.ble_spb)

        self.ble_vsl = QSlider(Form)
        self.ble_vsl.setObjectName(u"ble_vsl")
        self.ble_vsl.setMaximum(255)
        self.ble_vsl.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.ble_vsl)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)
        self.red_spb.valueChanged.connect(self.red_vsl.setValue)
        self.red_vsl.valueChanged.connect(self.red_spb.setValue)
        self.grn_spb.valueChanged.connect(self.grn_vsl.setValue)
        self.grn_vsl.valueChanged.connect(self.grn_spb.setValue)
        self.ble_spb.valueChanged.connect(self.ble_vsl.setValue)
        self.ble_vsl.valueChanged.connect(self.ble_spb.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.red_lbl.setText(QCoreApplication.translate("Form", u"Red", None))
        self.grn_lbl.setText(QCoreApplication.translate("Form", u"Green", None))
        self.ble_lbl.setText(QCoreApplication.translate("Form", u"Blue", None))
    # retranslateUi

