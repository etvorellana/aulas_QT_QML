# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crachaUupshb.ui'
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
        Form.resize(250, 400)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 250, 400))
        self.label.setPixmap(QPixmap(u"Imagens/modelo.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(55, 57, 130, 130))
        self.label_2.setPixmap(QPixmap(u"Imagens/pessoa.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 240, 171, 19))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 280, 181, 19))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Crach\u00e1", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Francisco Silva Oliveira", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Programador", None))
    # retranslateUi

