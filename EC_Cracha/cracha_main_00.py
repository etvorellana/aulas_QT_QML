import sys
from PySide2.QtWidgets import QApplication, QWidget
from ui_cracha import Ui_Form


class Cracha(Ui_Form, QWidget):     
    def __init__(self):
        super(Cracha, self).__init__()
        self.setupUi(self)

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Cracha()
    window.show()
    sys.exit(app.exec_())

