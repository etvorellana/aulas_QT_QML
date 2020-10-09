import sys

from PySide2.QtGui import QGuiApplication, QPixmap, QPainter
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide2.QtQuick import QQuickImageProvider
from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl
import qrcode
from PIL.ImageQt import ImageQt


class QRCImage(QQuickImageProvider):
    def __init__(self, data):
        QQuickImageProvider.__init__(self, QQuickImageProvider.Pixmap)
        self.__data = data
        self.__qrCode = None

    def requestPixmap(self, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        imgQt = ImageQt(img.convert("RGB"))   # keep a reference!
        pixmap = QPixmap.fromImage(imgQt)
        pixmap = pixmap.scaled(10, 10)
        return pixmap


    #data 
    dataChanged = Signal(str)

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
    
    data = Property(str, get_data, set_data, notify=dataChanged)

class Funcionario(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.__logo = "Imagens/logo.jpg"
        self.__nome_empresa = "Jabil do Brasil"
        self.__nome_funcionario = "Nome Funcionario"
        self.__img_funcionario = "Imagens/foto.png"
        

    def paint(self, painter):
        print(self.__qrCode)
        painter.drawPixmap(0,0,self.__qrCode)

    # logo
    logoChanged = Signal(str)
    def get_logo(self):
        return self.__logo
    
    logo = Property(str, get_logo, notify=logoChanged)

    # nomeEmpresa
    nomeEmpresaChanged = Signal(str)
    def get_nome_empresa(self):
        return self.__nome_empresa
    
    nomeEmpresa = Property(str, get_nome_empresa, notify=nomeEmpresaChanged)

    # nomeFuncionario
    nomeFuncionarioChanged = Signal(str)
    def get_nome_funcionario(self):
        return self.__nome_funcionario
    
    nomeFuncionario = Property(str, get_nome_funcionario, notify=nomeFuncionarioChanged)

    # imgFuncionario
    imgFuncionarioChanged = Signal(str)
    def get_img_funcionario(self):
        return self.__img_funcionario
    
    imgFuncionario = Property(str, get_img_funcionario, notify=imgFuncionarioChanged)

    # qrCode
    qrCodeChanged = Signal(str)
    def get_qrCode(self):
        return self.__qrCode
    
    qrCode = Property(str, get_qrCode, notify=qrCodeChanged)

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    #funcionario = Funcionario()
    #engine.rootContext().setContextProperty("funcionario", funcionario)
    qmlRegisterType(Funcionario, 'MyTools', 1, 0, 'Funcionario')
    qrcImage = QRCImage("Data")
    engine.addImageProvider("qrcode", qrcImage)
    
    engine.load(QUrl("Exercicio_01.qml"))
    
    if not engine.rootObjects():
        sys.exit(-1)    
    
    sys.exit(app.exec_())




