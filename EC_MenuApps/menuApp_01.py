# trabalhando com dock, status bar e toolbar

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QStatusBar,
                                QAction, QTextEdit, QToolBar, QDockWidget)
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, QSize

class menuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 350, 350)         
        self.setWindowTitle("Menu, Dock, Statusbar e Toolbar")  #Modificar o nome da Janela
        
        self.setCentralWidget(QTextEdit())

        self.createMenu()
        self.createToolBar()
        self.createDockWidget()
        
        self.show()

    def createMenu(self):
        """
        Criar barra e ações do menu
        """
        self.sair_act = QAction(QIcon('Imagens/exit.png'), 'Sair', self)
        self.sair_act.setShortcut('Ctrl+Q')
        self.sair_act.setStatusTip('Sair do programa')
        self.sair_act.triggered.connect(self.close)

        tela_cheia_act = QAction('Tela Cheia', self, checkable=True)
        tela_cheia_act.setStatusTip('Mudar para modo tela cheia')
        tela_cheia_act.triggered.connect(self.switchToFullScreen)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        arq_menu = menu_bar.addMenu('Arquivo')
        arq_menu.addAction(self.sair_act)

        vis_menu = menu_bar.addMenu('Visualizar')
        apar_smenu = vis_menu.addMenu('Aparência')
        apar_smenu.addAction(tela_cheia_act)

        self.setStatusBar(QStatusBar(self))

    def createToolBar(self):
        """
        Criar barra de ferramentas
        """
        tool_bar = QToolBar("Barra de Ferramentas")
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)

        tool_bar.addAction(self.sair_act)

    def createDockWidget(self):
        """
        Criar dock
        """
        dock_wgt = QDockWidget()
        dock_wgt.setWindowTitle("Dock Exemplo")
        dock_wgt.setAllowedAreas(Qt.AllDockWidgetAreas)

        dock_wgt.setWidget(QTextEdit())

        self.addDockWidget(Qt.LeftDockWidgetArea, dock_wgt)

    def switchToFullScreen(self, state):
        """
        Se o estado for True, exiba a janela principal em tela 
        inteira. Caso contrário, retorne a janela ao normal.
        """
        if state:
            self.showFullScreen()
        else:
            self.showNormal()


#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = menuApp()
    sys.exit(app.exec_())
