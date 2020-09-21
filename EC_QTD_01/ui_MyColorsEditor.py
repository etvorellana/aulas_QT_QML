# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyColorsEditorlAsxXe.ui'
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
        Form.resize(473, 542)
        self.horizontalLayout = QHBoxLayout(Form)
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
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

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
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.ble_spb = QSpinBox(Form)
        self.ble_spb.setObjectName(u"ble_spb")

        self.verticalLayout_3.addWidget(self.ble_spb)

        self.ble_vls = QSlider(Form)
        self.ble_vls.setObjectName(u"ble_vls")
        self.ble_vls.setMaximum(255)
        self.ble_vls.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.ble_vls)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)
        self.red_spb.valueChanged.connect(self.red_vsl.setValue)
        self.red_vsl.valueChanged.connect(self.red_spb.setValue)
        self.grn_spb.valueChanged.connect(self.grn_vsl.setValue)
        self.grn_vsl.valueChanged.connect(self.grn_spb.setValue)
        self.ble_spb.valueChanged.connect(self.ble_vls.setValue)
        self.ble_vls.valueChanged.connect(self.ble_spb.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.red_lbl.setText(QCoreApplication.translate("Form", u"Red", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Green", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Blue", None))
    # retranslateUi

