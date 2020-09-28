# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tempAmbiente_V2kpJRvP.ui'
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

import temAmbiente_rc

class Ui_temAmbiente(object):
    def setupUi(self, temAmbiente):
        if not temAmbiente.objectName():
            temAmbiente.setObjectName(u"temAmbiente")
        temAmbiente.resize(959, 600)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        temAmbiente.setFont(font)
        self.novo_act = QAction(temAmbiente)
        self.novo_act.setObjectName(u"novo_act")
        icon = QIcon()
        icon.addFile(u":/Iconnes/file/filenew.png", QSize(), QIcon.Normal, QIcon.Off)
        self.novo_act.setIcon(icon)
        self.abre_act = QAction(temAmbiente)
        self.abre_act.setObjectName(u"abre_act")
        icon1 = QIcon()
        icon1.addFile(u":/Iconnes/file/fileopen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.abre_act.setIcon(icon1)
        self.salva_act = QAction(temAmbiente)
        self.salva_act.setObjectName(u"salva_act")
        icon2 = QIcon()
        icon2.addFile(u":/Iconnes/file/filesave.png", QSize(), QIcon.Normal, QIcon.On)
        self.salva_act.setIcon(icon2)
        self.slvcm_act = QAction(temAmbiente)
        self.slvcm_act.setObjectName(u"slvcm_act")
        icon3 = QIcon()
        icon3.addFile(u":/Iconnes/file/filesaveas.png", QSize(), QIcon.Normal, QIcon.On)
        self.slvcm_act.setIcon(icon3)
        self.sair_act = QAction(temAmbiente)
        self.sair_act.setObjectName(u"sair_act")
        icon4 = QIcon()
        icon4.addFile(u":/Iconnes/file/fileclose.png", QSize(), QIcon.Normal, QIcon.On)
        self.sair_act.setIcon(icon4)
        self.senin_act = QAction(temAmbiente)
        self.senin_act.setObjectName(u"senin_act")
        self.senex_act = QAction(temAmbiente)
        self.senex_act.setObjectName(u"senex_act")
        self.mod_act = QAction(temAmbiente)
        self.mod_act.setObjectName(u"mod_act")
        self.ams_act = QAction(temAmbiente)
        self.ams_act.setObjectName(u"ams_act")
        self.log_act = QAction(temAmbiente)
        self.log_act.setObjectName(u"log_act")
        self.log_act.setCheckable(True)
        self.log_act.setChecked(True)
        self.ajs_act = QAction(temAmbiente)
        self.ajs_act.setObjectName(u"ajs_act")
        self.ajs_act.setEnabled(False)
        self.col_act = QAction(temAmbiente)
        self.col_act.setObjectName(u"col_act")
        self.aval_act = QAction(temAmbiente)
        self.aval_act.setObjectName(u"aval_act")
        self.aval_act.setEnabled(False)
        self.sbre_act = QAction(temAmbiente)
        self.sbre_act.setObjectName(u"sbre_act")
        self.centralwidget = QWidget(temAmbiente)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.graphicsView = QGraphicsView(self.frame)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_7.addWidget(self.graphicsView)


        self.verticalLayout_5.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCheckable(False)

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setCheckable(False)

        self.verticalLayout_3.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_4)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_4.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_4.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_4.addWidget(self.radioButton_4)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        temAmbiente.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(temAmbiente)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 29))
        self.arqv_mnu = QMenu(self.menubar)
        self.arqv_mnu.setObjectName(u"arqv_mnu")
        self.conf_mnu = QMenu(self.menubar)
        self.conf_mnu.setObjectName(u"conf_mnu")
        self.ferr_mnu = QMenu(self.menubar)
        self.ferr_mnu.setObjectName(u"ferr_mnu")
        self.ajud_mnu = QMenu(self.menubar)
        self.ajud_mnu.setObjectName(u"ajud_mnu")
        temAmbiente.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(temAmbiente)
        self.statusbar.setObjectName(u"statusbar")
        temAmbiente.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(temAmbiente)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        temAmbiente.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QDockWidget(temAmbiente)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.int_sbt = QSpinBox(self.dockWidgetContents)
        self.int_sbt.setObjectName(u"int_sbt")
        self.int_sbt.setMinimum(6)
        self.int_sbt.setMaximum(24)

        self.verticalLayout.addWidget(self.int_sbt)

        self.int_lbl = QLabel(self.dockWidgetContents)
        self.int_lbl.setObjectName(u"int_lbl")
        self.int_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.int_lbl)

        self.col_btn = QPushButton(self.dockWidgetContents)
        self.col_btn.setObjectName(u"col_btn")

        self.verticalLayout.addWidget(self.col_btn)

        self.aju_btn = QPushButton(self.dockWidgetContents)
        self.aju_btn.setObjectName(u"aju_btn")
        self.aju_btn.setEnabled(False)

        self.verticalLayout.addWidget(self.aju_btn)

        self.ava_btn = QPushButton(self.dockWidgetContents)
        self.ava_btn.setObjectName(u"ava_btn")
        self.ava_btn.setEnabled(False)

        self.verticalLayout.addWidget(self.ava_btn)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.clock_lbl = QLabel(self.dockWidgetContents)
        self.clock_lbl.setObjectName(u"clock_lbl")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.clock_lbl.setFont(font1)
        self.clock_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.clock_lbl)

        self.data_lbl = QLabel(self.dockWidgetContents)
        self.data_lbl.setObjectName(u"data_lbl")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(18)
        self.data_lbl.setFont(font2)
        self.data_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.data_lbl)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_10 = QLabel(self.dockWidgetContents)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setBold(False)
        font3.setWeight(50)
        self.label_10.setFont(font3)

        self.gridLayout.addWidget(self.label_10, 1, 3, 1, 1)

        self.label_9 = QLabel(self.dockWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)

        self.label_15 = QLabel(self.dockWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_5 = QLabel(self.dockWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)

        self.label_11 = QLabel(self.dockWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.gridLayout.addWidget(self.label_11, 2, 3, 1, 1)

        self.label_17 = QLabel(self.dockWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_12 = QLabel(self.dockWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.gridLayout.addWidget(self.label_12, 2, 1, 1, 1)

        self.label_16 = QLabel(self.dockWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_7 = QLabel(self.dockWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_3 = QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_8 = QLabel(self.dockWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_13 = QLabel(self.dockWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)

        self.label_6 = QLabel(self.dockWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)

        self.label_14 = QLabel(self.dockWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.gridLayout.addWidget(self.label_14, 3, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.dockWidget.setWidget(self.dockWidgetContents)
        temAmbiente.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.arqv_mnu.menuAction())
        self.menubar.addAction(self.conf_mnu.menuAction())
        self.menubar.addAction(self.ferr_mnu.menuAction())
        self.menubar.addAction(self.ajud_mnu.menuAction())
        self.arqv_mnu.addAction(self.novo_act)
        self.arqv_mnu.addAction(self.abre_act)
        self.arqv_mnu.addAction(self.salva_act)
        self.arqv_mnu.addAction(self.slvcm_act)
        self.arqv_mnu.addSeparator()
        self.arqv_mnu.addAction(self.sair_act)
        self.conf_mnu.addAction(self.senin_act)
        self.conf_mnu.addAction(self.senex_act)
        self.conf_mnu.addSeparator()
        self.conf_mnu.addAction(self.mod_act)
        self.conf_mnu.addAction(self.ams_act)
        self.conf_mnu.addAction(self.log_act)
        self.ferr_mnu.addAction(self.col_act)
        self.ferr_mnu.addAction(self.ajs_act)
        self.ferr_mnu.addAction(self.aval_act)
        self.ajud_mnu.addAction(self.sbre_act)
        self.toolBar.addAction(self.novo_act)
        self.toolBar.addAction(self.abre_act)
        self.toolBar.addAction(self.salva_act)
        self.toolBar.addAction(self.slvcm_act)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.sair_act)

        self.retranslateUi(temAmbiente)

        QMetaObject.connectSlotsByName(temAmbiente)
    # setupUi

    def retranslateUi(self, temAmbiente):
        temAmbiente.setWindowTitle(QCoreApplication.translate("temAmbiente", u"Monitor de Temperatura Ambiente", None))
        self.novo_act.setText(QCoreApplication.translate("temAmbiente", u"Novo", None))
#if QT_CONFIG(tooltip)
        self.novo_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Criar um novo modelo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.novo_act.setShortcut(QCoreApplication.translate("temAmbiente", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.abre_act.setText(QCoreApplication.translate("temAmbiente", u"Abrir", None))
#if QT_CONFIG(tooltip)
        self.abre_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Abrir modelo ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.abre_act.setShortcut(QCoreApplication.translate("temAmbiente", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.salva_act.setText(QCoreApplication.translate("temAmbiente", u"Salvar", None))
#if QT_CONFIG(tooltip)
        self.salva_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Salvar modelo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.salva_act.setShortcut(QCoreApplication.translate("temAmbiente", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.slvcm_act.setText(QCoreApplication.translate("temAmbiente", u"Salvar Como", None))
#if QT_CONFIG(tooltip)
        self.slvcm_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Salvar modelo como", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.slvcm_act.setShortcut(QCoreApplication.translate("temAmbiente", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.sair_act.setText(QCoreApplication.translate("temAmbiente", u"Sair", None))
#if QT_CONFIG(tooltip)
        self.sair_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Sair", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.sair_act.setShortcut(QCoreApplication.translate("temAmbiente", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.senin_act.setText(QCoreApplication.translate("temAmbiente", u"Sensor Internos", None))
#if QT_CONFIG(tooltip)
        self.senin_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Configurar sensor interno a ser utilizado", None))
#endif // QT_CONFIG(tooltip)
        self.senex_act.setText(QCoreApplication.translate("temAmbiente", u"Sensor Refer\u00eancia", None))
#if QT_CONFIG(tooltip)
        self.senex_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Selecionar sensor de refer\u1ebdncia", None))
#endif // QT_CONFIG(tooltip)
        self.mod_act.setText(QCoreApplication.translate("temAmbiente", u"Modelo", None))
#if QT_CONFIG(tooltip)
        self.mod_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Selecionar modelo de ajuste", None))
#endif // QT_CONFIG(tooltip)
        self.ams_act.setText(QCoreApplication.translate("temAmbiente", u"Amostragem", None))
#if QT_CONFIG(tooltip)
        self.ams_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Selecionar intervalo de amostragem de temperatura", None))
#endif // QT_CONFIG(tooltip)
        self.log_act.setText(QCoreApplication.translate("temAmbiente", u"Manter Log", None))
#if QT_CONFIG(tooltip)
        self.log_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Manter log de temperatura", None))
#endif // QT_CONFIG(tooltip)
        self.ajs_act.setText(QCoreApplication.translate("temAmbiente", u"Ajustar", None))
#if QT_CONFIG(tooltip)
        self.ajs_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Ajustar modelo com dados coletados", None))
#endif // QT_CONFIG(tooltip)
        self.col_act.setText(QCoreApplication.translate("temAmbiente", u"Coletar", None))
#if QT_CONFIG(tooltip)
        self.col_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Coletar dados para ajuste", None))
#endif // QT_CONFIG(tooltip)
        self.aval_act.setText(QCoreApplication.translate("temAmbiente", u"Avaliar", None))
#if QT_CONFIG(tooltip)
        self.aval_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Coletar dados para avaliar o modelo", None))
#endif // QT_CONFIG(tooltip)
        self.sbre_act.setText(QCoreApplication.translate("temAmbiente", u"Sobre", None))
#if QT_CONFIG(tooltip)
        self.sbre_act.setToolTip(QCoreApplication.translate("temAmbiente", u"Detalhes do software", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("temAmbiente", u"Curvas no gr\u00e1fico", None))
        self.checkBox.setText(QCoreApplication.translate("temAmbiente", u"Temperatura estimada", None))
        self.checkBox_2.setText(QCoreApplication.translate("temAmbiente", u"Temperatura sensor interno", None))
        self.checkBox_3.setText(QCoreApplication.translate("temAmbiente", u"Temperatura sensor de refer\u00eancia", None))
        self.checkBox_4.setText(QCoreApplication.translate("temAmbiente", u"Atividade do dispositivo", None))
        self.label_2.setText(QCoreApplication.translate("temAmbiente", u"Intervalo de monitoramento", None))
        self.radioButton.setText(QCoreApplication.translate("temAmbiente", u"1 hora", None))
        self.radioButton_2.setText(QCoreApplication.translate("temAmbiente", u"6 horas", None))
        self.radioButton_3.setText(QCoreApplication.translate("temAmbiente", u"12 horas", None))
        self.radioButton_4.setText(QCoreApplication.translate("temAmbiente", u"24 horas", None))
        self.arqv_mnu.setTitle(QCoreApplication.translate("temAmbiente", u"Arquivo", None))
        self.conf_mnu.setTitle(QCoreApplication.translate("temAmbiente", u"Configura\u00e7\u00f5es", None))
        self.ferr_mnu.setTitle(QCoreApplication.translate("temAmbiente", u"Ferramentas", None))
        self.ajud_mnu.setTitle(QCoreApplication.translate("temAmbiente", u"Ajuda", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("temAmbiente", u"toolBar", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("temAmbiente", u"Ferramentas", None))
        self.int_sbt.setSuffix(QCoreApplication.translate("temAmbiente", u" Horas", None))
        self.int_lbl.setText(QCoreApplication.translate("temAmbiente", u"Intervalo de coleta", None))
        self.col_btn.setText(QCoreApplication.translate("temAmbiente", u"Coletar", None))
        self.aju_btn.setText(QCoreApplication.translate("temAmbiente", u"Ajustar", None))
        self.ava_btn.setText(QCoreApplication.translate("temAmbiente", u"Avaliar", None))
        self.clock_lbl.setText(QCoreApplication.translate("temAmbiente", u"00:00", None))
        self.data_lbl.setText(QCoreApplication.translate("temAmbiente", u"DD/MM/AAAA", None))
        self.label_4.setText(QCoreApplication.translate("temAmbiente", u"M\u00ednima \u00baC", None))
        self.label_10.setText(QCoreApplication.translate("temAmbiente", u"35", None))
        self.label_9.setText(QCoreApplication.translate("temAmbiente", u"35", None))
        self.label_15.setText(QCoreApplication.translate("temAmbiente", u"Estimada", None))
        self.label_5.setText(QCoreApplication.translate("temAmbiente", u"Media \u00baC", None))
        self.label_11.setText(QCoreApplication.translate("temAmbiente", u"35", None))
        self.label_17.setText(QCoreApplication.translate("temAmbiente", u"Refer\u00eancia", None))
        self.label_12.setText(QCoreApplication.translate("temAmbiente", u"35", None))
        self.label_16.setText(QCoreApplication.translate("temAmbiente", u"Interna", None))
        self.label_7.setText(QCoreApplication.translate("temAmbiente", u"35", None))
        self.label_3.setText(QCoreApplication.translate("temAmbiente", u"M\u00e1xima \u00baC", None))
        self.label_8.setText(QCoreApplication.translate("temAmbiente", u"35", None))
        self.label_13.setText(QCoreApplication.translate("temAmbiente", u"35", None))
        self.label_6.setText(QCoreApplication.translate("temAmbiente", u"35", None))
        self.label_14.setText(QCoreApplication.translate("temAmbiente", u"35", None))
    # retranslateUi

