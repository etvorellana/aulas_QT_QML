# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dispHorariosFqssiz.ui'
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
        DispHoras.resize(348, 345)
        self.horizontalLayout = QHBoxLayout(DispHoras)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.quest_lbl = QLabel(DispHoras)
        self.quest_lbl.setObjectName(u"quest_lbl")
        self.quest_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.quest_lbl)

        self.mat_chbx = QCheckBox(DispHoras)
        self.mat_chbx.setObjectName(u"mat_chbx")
        self.mat_chbx.setChecked(True)

        self.verticalLayout.addWidget(self.mat_chbx)

        self.ves_chbx = QCheckBox(DispHoras)
        self.ves_chbx.setObjectName(u"ves_chbx")

        self.verticalLayout.addWidget(self.ves_chbx)

        self.not_chbx = QCheckBox(DispHoras)
        self.not_chbx.setObjectName(u"not_chbx")

        self.verticalLayout.addWidget(self.not_chbx)

        self.fechar_btn = QPushButton(DispHoras)
        self.fechar_btn.setObjectName(u"fechar_btn")

        self.verticalLayout.addWidget(self.fechar_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(DispHoras)
        self.fechar_btn.pressed.connect(DispHoras.close)

        QMetaObject.connectSlotsByName(DispHoras)
    # setupUi

    def retranslateUi(self, DispHoras):
        DispHoras.setWindowTitle(QCoreApplication.translate("DispHoras", u"Disponibilidade de Hor\u00e1rio", None))
        self.quest_lbl.setText(QCoreApplication.translate("DispHoras", u"Em quais turnos voc\u00ea pode trabalhar? (Verifque antes de confirmar)", None))
        self.mat_chbx.setText(QCoreApplication.translate("DispHoras", u"Matutino [8:00 - 14:00]", None))
        self.ves_chbx.setText(QCoreApplication.translate("DispHoras", u"Vespertino [14:00 - 20:00]", None))
        self.not_chbx.setText(QCoreApplication.translate("DispHoras", u"Noturno [20:00 - 2:00]", None))
        self.fechar_btn.setText(QCoreApplication.translate("DispHoras", u"Fechar", None))
    # retranslateUi

