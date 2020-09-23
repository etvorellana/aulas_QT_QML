import sys
from PySide2.QtWidgets import QApplication, QWidget
from ui_Exemplo_01 import Ui_Form


class CorApp(Ui_Form, QWidget):     
    def __init__(self):
        super(CorApp, self).__init__()
        self.setupUi(self)

#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CorApp()
    window.show()
    sys.exit(app.exec_())