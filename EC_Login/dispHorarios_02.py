# Importando do código Python gerado pelo Qt Designer

import sys
import os

from PySide2.QtWidgets import QApplication, QWidget, QCheckBox
from ui_dispHorarios import Ui_DispHoras
from PySide2.QtCore import Qt, QFile
from PySide2.QtUiTools import QUiLoader


class DispHoras(QWidget):
    def __init__(self):
        super(DispHoras, self).__init__()
        #Carrega a UI diretamente do arquivo 
        self.load_ui()

        # Cria os componentes com base naqueles da UI
        self.ves_chbx = self.findChild(QCheckBox, 'ves_chbx')
        self.mat_chbx = self.findChild(QCheckBox, 'mat_chbx')
        self.not_chbx = self.findChild(QCheckBox, 'not_chbx')

        # Conectar os sinais com o slot
        self.ves_chbx.stateChanged.connect(self.printToTerminal)
        self.mat_chbx.stateChanged.connect(self.printToTerminal)
        self.not_chbx.stateChanged.connect(self.printToTerminal)

    #Carrega a UI utilizando o QUiLoader
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "dispHorarios.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    #Implementando o slot
    def printToTerminal(self, state):
        """
        Mostra como determinar o estado de um checkbox
        Imprime no terminal o texto do widget que mandou
        o sinal
        """

        sender = self.sender()
        if state == Qt.Checked:
            print("{} Selecionado.".format(sender.text()))
        else:
            print("{} Recusado.".format(sender.text()))


#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DispHoras()
    window.show()
    sys.exit(app.exec_())
