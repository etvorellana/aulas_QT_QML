
# Mostrando o qrCode

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QPixmap
from PIL.ImageQt import ImageQt
import qrcode

class JDaApp(QWidget):

    def __init__(self):
        super().__init__() # chamada ao construtor padrão da superclasse
        self.iniciaUI()

    def iniciaUI(self):
        """
        Inicializa a janela e mostra seu conteuda na tela
        """

        self.setGeometry(100,100, 250, 250)
        self.setWindowTitle("Crachá")
        self.displayLabels()

        self.show()

    def displayLabels(self):
        """
        Apresentando texto e imagens com QLabels.

        Verifica se o arquivo de imagem está disponível,
        caso contrario gera uma exception.
        """

        txt_lbl = QLabel(self)
        txt_lbl.setText("Saudações")
        txt_lbl.move(95, 15)

        #img = "Imagens/pessoa.png"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data("Esbel Tomas Valero Orellana, ")
        qr.add_data("Professor Pleno, ")
        qr.add_data("evalero@uesc.br")
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        imgQt = ImageQt(img.convert("RGB"))   # keep a reference!
        pixmap = QPixmap.fromImage(imgQt)
        #self.setPixmap(pixm.scaled(self.size(),QtCore.Qt.KeepAspectRatio))
        
        pic_lbl = QLabel(self)
        #pixmap = QPixmap(img)
        pixmap = pixmap.scaled(160, 160)
        pic_lbl.setPixmap(pixmap)
        pic_lbl.move(45, 45)
    
#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JDaApp()
    sys.exit(app.exec_())

