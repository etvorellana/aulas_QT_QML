# photoeditor.py

import sys
from PySide2.QtWidgets import  (QApplication, QMainWindow, QWidget, 
                                QLabel, QAction, QFileDialog, 
                                QDesktopWidget, QMessageBox, QSizePolicy, 
                                QToolBar, QStatusBar, QDockWidget, 
                                QVBoxLayout, QPushButton)
from PySide2.QtGui import  QIcon, QPixmap, QTransform, QPainter
from PySide2.QtCore import Qt, QSize, QRect
from PySide2.QtPrintSupport import QPrinter, QPrintDialog


class PhotoEditor(QMainWindow): #Ok
    def __init__(self):
        super().__init__()
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setFixedSize(650, 650)
        #self.setGeometry(100,100, 400, 230)
        self.setWindowTitle("Photo Editor")
        self.centerMainWindow()
        self.createToolsDockWidget()
        self.createMenu()
        self.createToolBar()
        self.photoEditorWidgets()

        self.show()

    def centerMainWindow(self): #Ok
        """
        Use a classe QDesktopWidget para acessar informações sobre 
        sua tela e use-a para centralizar a janela do aplicativo.
        """
        desktop = QDesktopWidget().screenGeometry()
        screen_width = desktop.width()
        screen_height = desktop.height()
        self.move((screen_width - self.width()) / 2, 
                    (screen_height - self.height()) / 2)

    def createMenu(self): #Ok
        """
        Criar menu para editor de fotos
        """

        self.abre_act = QAction(QIcon('Imagens/open_file.png'),"Abrir", self)
        self.abre_act.setShortcut('Ctrl+O')
        self.abre_act.setStatusTip('Abrir uma nova imagem')
        self.abre_act.triggered.connect(self.openImage)

        self.salv_act = QAction(QIcon('Imagens/save_file.png'), 'Salvar', self)
        self.salv_act.setShortcut('Ctrl+S')
        self.salv_act.setStatusTip('Salvar imagem')
        self.salv_act.triggered.connect(self.saveToFile)

        self.prnt_act = QAction(QIcon('Imagens/print.png'), "Imprimir", self)
        self.prnt_act.setShortcut('Ctrl+P')
        self.prnt_act.setStatusTip('Imprimir imagem')
        self.prnt_act.triggered.connect(self.printImage)
        self.prnt_act.setEnabled(False)

        self.sair_act = QAction(QIcon('Imagens/exit.png'), 'Sair', self)
        self.sair_act.setShortcut('Ctrl+Q')
        self.sair_act.setStatusTip('Sair do programa')
        self.sair_act.triggered.connect(self.close)
        
        self.rt90_act = QAction("Girar 90°", self)
        self.rt90_act.setStatusTip('Girar imagem 90 ° no sentido horário') 
        self.rt90_act.triggered.connect(self.rotateImage90)

        self.rt180_act = QAction("Girar 180°", self)
        self.rt180_act.setStatusTip('Girar imagem 180° no sentido horário') 
        self.rt180_act.triggered.connect(self.rotateImage180)

        self.flph_act = QAction("Espelhar na Horizontal", self)
        self.flph_act.setStatusTip('Espelhar imagem no eixo horizontal')
        self.flph_act.triggered.connect(self.flipImageHorizontal)

        self.flpv_act = QAction("Espelhar na Vertical", self)
        self.flpv_act.setStatusTip('Espelhar imagem no eixo vertical')
        self.flpv_act.triggered.connect(self.flipImageVertical)

        self.redm_act = QAction("Redimensionar metade", self)
        self.redm_act.setStatusTip('Redimensionar imagem para metade do tamanho original')
        self.redm_act.triggered.connect(self.resizeImageHalf)

        self.limp_act = QAction(QIcon('Imagens/clear.png'), "Limpar Imagem", self)
        self.limp_act.setShortcut("Ctrl+D")
        self.limp_act.setStatusTip('Limpar a imagem atual')
        self.limp_act.triggered.connect(self.clearImage)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        arqv_menu = menu_bar.addMenu('Arquivo')
        arqv_menu.addAction(self.abre_act)
        arqv_menu.addAction(self.salv_act)
        arqv_menu.addSeparator()
        arqv_menu.addAction(self.prnt_act)
        arqv_menu.addSeparator()
        arqv_menu.addAction(self.sair_act)

        edit_menu = menu_bar.addMenu('Editar')
        edit_menu.addAction(self.rt90_act)
        edit_menu.addAction(self.rt180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flph_act)
        edit_menu.addAction(self.flpv_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.redm_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.limp_act)

        #???????????????????
        view_menu = menu_bar.addMenu('Exibir')
        view_menu.addAction(self.toggle_dock_tools_act)

        self.setStatusBar(QStatusBar(self))
 
    def openImage(self): #Ok
        """
        Abrir um arquivo de imagem e exiba seu conteúdo 
        no label.
        Exibir mensagem de erro se a imagem não puder ser aberta.
        """
        arq_img, _ = QFileDialog.getOpenFileName(self, "Abrir Imagem", "",
                        "Arquivos JPG (*.jpeg *.jpg );;Arquivos PNG (*.png)\
                            ;;Arquivos  Bitmap (*.bmp);;Arquivos  GIF (*.gif)")

        if arq_img:
            self.img = QPixmap(arq_img)
            self.img_lbl.setPixmap(self.img.scaled(self.img_lbl.size(),
                            Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            QMessageBox.information(self, "Erro", "Não é possível abrir imagem.", 
                                QMessageBox.Ok)     

        self.prnt_act.setEnabled(True)   

    def saveToFile(self): #Ok
        """
        Salvar a imagem.
        Exibir mensagem de erro se a imagem não puder ser salva.
        """
        
        arq_img, _ = QFileDialog.getSaveFileName(self, "Salvar Imagem", "",
                        "Arquivos JPG (*.jpeg *.jpg );;Arquivos PNG (*.png)\
                            ;;Arquivos  Bitmap (*.bmp);;Arquivos  GIF (*.gif)")
        
        if arq_img and self.img.isNull() == False:
            self.img.save(image_file)
        else:
            QMessageBox.information(self, "Não é possível salvar imagem.", 
                                QMessageBox.Ok)   

    def printImage(self): #Ok
        """Imprimir Imagem
        """
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.NativeFormat)

        prnt_dlg = QPrintDialog(printer)

        if (prnt_dlg.exec_() == QPrintDialog.Accepted):
            
            painter = QPainter()

            painter.begin(printer)

            rect = QRect(painter.viewport())

            size = QSize(self.img_lbl.pixmap().size())
            size.scale(rect.size(), Qt.KeepAspectRatio)
        
            painter.setViewport(rect.x(), rect.y(), size.width(), 
                size.height())
            painter.setWindow(self.img_lbl.pixmap().rect())

            painter.drawPixmap(0, 0, self.img_lbl.pixmap())

            painter.end()

    def rotateImage90(self): #Ok
        """
        Girar imagem 90° no sentido horário
        """
        if self.img.isNull() == False:
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.img)
            rotated = pixmap.transformed(transform90, 
                        mode=Qt.SmoothTransformation)
            self.img_lbl.setPixmap(rotated.scaled(self.img_lbl.size(),
                            Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.img = QPixmap(rotated)
            self.img_lbl.repaint() # repaint the child widget
        else:
            # No image to rotate
            pass

    def rotateImage180(self): #Ok
        """
        Girar imagem 180° no sentido horário
        """
        if self.img.isNull() == False:
            transform180 = QTransform().rotate(180)
            pixmap = QPixmap(self.img)
            rotated = pixmap.transformed(transform180, 
                        mode=Qt.SmoothTransformation)
            self.img_lbl.setPixmap(rotated.scaled(self.img_lbl.size(),
                            Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.img = QPixmap(rotated)
            self.img_label.repaint() # repaint the child widget
        else:
            # No image to rotate
            pass

    def flipImageHorizontal(self): #Ok
        """
        Espelhar a imagem no eixo horizontal
        """
        if self.img.isNull() == False:
            flip_h = QTransform().scale(-1, 1)
            pixmap = QPixmap(self.img)
            flipped = pixmap.transformed(flip_h)
            self.img_lbl.setPixmap(flipped.scaled(self.img_lbl.size(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.img = QPixmap(flipped)
            self.img_lbl.repaint()
        else:
            pass

    def flipImageVertical(self): #Ok
        """
        Espelhar a imagem no eixo vertical
        """
        if self.img.isNull() == False:
            flip_v = QTransform().scale(1, -1)
            pixmap = QPixmap(self.img)
            flipped = pixmap.transformed(flip_v)
            self.img_lbl.setPixmap(flipped.scaled(self.img_lbl.size(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.img = QPixmap(flipped)
            self.img_lbl.repaint()
        else:
            pass

    def resizeImageHalf(self): #Ok
        """
        Redimensione a imagem para a metade do tamanho atual.
        """
        if self.img.isNull() == False:
            resize = QTransform().scale(0.5, 0.5)
            pixmap = QPixmap(self.img)
            resized = pixmap.transformed(resize)
            self.img_lbl.setPixmap(resized.scaled(self.img_lbl.size(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.img = QPixmap(resized)
            self.img_lbl.repaint()
        else:
            pass

    def clearImage(self): #Ok
        """
        Limpar a imagem atual no widget QLabel
        """
        self.img_lbl.clear()
        self.img = QPixmap()
    
    def createToolBar(self): #Ok
        """
        Criar barra de ferramentas para editor de fotos
        """
        tool_bar = QToolBar("Barra de Ferramentas do Editor de Fotos")
        tool_bar.setIconSize(QSize(24,24)) 
        self.addToolBar(tool_bar)

        tool_bar.addAction(self.abre_act)
        tool_bar.addAction(self.salv_act)
        tool_bar.addAction(self.prnt_act)
        tool_bar.addAction(self.limp_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.sair_act)

    def createToolsDockWidget(self): #Ok
        """
        Use o menu Exibir -> Editar Ferramentas de Imagem e clique
        no widget dock para ligar ou desligar. 
        O dock de ferramentas pode ser colocado à esquerda ou à 
        direita da janela principal.
        """

        self.dock_tools_view = QDockWidget()
        self.dock_tools_view.setWindowTitle("Ferramentas Edição de Imagem")
        self.dock_tools_view.setAllowedAreas(Qt.LeftDockWidgetArea |
                                                Qt.RightDockWidgetArea)

        self.img_tool = QWidget()

        self.rt90_btn = QPushButton("Girar 90°")
        self.rt90_btn.setMinimumSize(QSize(130, 40))
        self.rt90_btn.setStatusTip('Girar imagem 90° no sentido horário')
        self.rt90_btn.clicked.connect(self.rotateImage90)

        self.rt180_btn = QPushButton("Girar 180°")
        self.rt180_btn.setMinimumSize(QSize(130, 40))
        self.rt180_btn.setStatusTip('Girar imagem 180° no sentido horário')
        self.rt180_btn.clicked.connect(self.rotateImage180)

        self.flph_btn = QPushButton("Espelhar na Horizontal")
        self.flph_btn.setMinimumSize(QSize(130, 40))
        self.flph_btn.setStatusTip('Espelhar imagem no eixo horizontal')
        self.flph_btn.clicked.connect(self.flipImageHorizontal)

        self.flpv_btn = QPushButton("Espelhar na Vertical")
        self.flpv_btn.setMinimumSize(QSize(130, 40))
        self.flpv_btn.setStatusTip('Espelhar imagem no eixo vertical')
        self.flpv_btn.clicked.connect(self.flipImageVertical)

        self.redm_btn = QPushButton("Redimensionar metade")
        self.redm_btn.setMinimumSize(QSize(130, 40))
        self.redm_btn.setStatusTip('Redimensionar imagem para metade do tamanho original')
        self.redm_btn.clicked.connect(self.resizeImageHalf)

        vbox = QVBoxLayout()
        vbox.addWidget(self.rt90_btn)
        vbox.addWidget(self.rt180_btn)
        vbox.addStretch(1)
        vbox.addWidget(self.flph_btn)
        vbox.addWidget(self.flpv_btn)
        vbox.addStretch(1)
        vbox.addWidget(self.redm_btn)
        vbox.addStretch(6)

        self.img_tool.setLayout(vbox)
        self.dock_tools_view.setWidget(self.img_tool)

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_tools_view)

        self.toggle_dock_tools_act = self.dock_tools_view.toggleViewAction()
        
    def photoEditorWidgets(self): #Ok
        """
        Configurar instâncias de widgets para editor de fotos
        """
        
        self.img = QPixmap()
        self.img_lbl = QLabel()
        self.img_lbl.setAlignment(Qt.AlignCenter)
        self.img_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)

        self.setCentralWidget(self.img_lbl)



#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhotoEditor()
    sys.exit(app.exec_())
