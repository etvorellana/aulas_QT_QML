# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader



class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.load_ui()

        self.lmpr_btn = self.findChild(QPushButton, 'lmpr_btn')
        self.nome_edln = self.findChild(QLineEdit, 'nome_edln')
        
        self.lmpr_btn.clicked.connect(self.limparCxTxt)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


    def limparCxTxt(self):
        """
        Quando acionado o butão limpa a caixa de texto
        """

        sender = self.sender()
        if sender.text() == 'Limpar':
            self.nome_edln.clear()



if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())
