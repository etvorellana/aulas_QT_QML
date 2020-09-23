# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dispHorariosDxkEeF.ui'
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


class Ui_DispHoras(object):
    def setupUi(self, DispHoras):
        if not DispHoras.objectName():
            DispHoras.setObjectName(u"DispHoras")
        DispHoras.resize(250, 251)
        self.verticalLayout = QVBoxLayout(DispHoras)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vlyt = QVBoxLayout()
        self.vlyt.setObjectName(u"vlyt")
        self.label = QLabel(DispHoras)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.vlyt.addWidget(self.label)

        self.mat_chbx = QCheckBox(DispHoras)
        self.mat_chbx.setObjectName(u"mat_chbx")
        self.mat_chbx.setChecked(True)

        self.vlyt.addWidget(self.mat_chbx)

        self.ves_chbx = QCheckBox(DispHoras)
        self.ves_chbx.setObjectName(u"ves_chbx")

        self.vlyt.addWidget(self.ves_chbx)

        self.not_chbx = QCheckBox(DispHoras)
        self.not_chbx.setObjectName(u"not_chbx")

        self.vlyt.addWidget(self.not_chbx)


        self.verticalLayout.addLayout(self.vlyt)


        self.retranslateUi(DispHoras)

        QMetaObject.connectSlotsByName(DispHoras)
    # setupUi

    def retranslateUi(self, DispHoras):
        DispHoras.setWindowTitle(QCoreApplication.translate("DispHoras", u"Disponibilidade de Hor\u00e1rio", None))
        self.label.setText(QCoreApplication.translate("DispHoras", u"Em quais turnos voc\u00ea pode trabalhar? (Verifque antes de confirmar)", None))
        self.mat_chbx.setText(QCoreApplication.translate("DispHoras", u"Matutino [8:00 - 14:00]", None))
        self.ves_chbx.setText(QCoreApplication.translate("DispHoras", u"Vespertino [14:00 - 20:00]", None))
        self.not_chbx.setText(QCoreApplication.translate("DispHoras", u"Noturno [20:00 - 2:00]", None))
    # retranslateUi

