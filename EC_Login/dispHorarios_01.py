# Importando do código Python gerado pelo Qt Designer

import sys
from PySide2.QtWidgets import QApplication, QWidget
from ui_dispHorarios import Ui_DispHoras
from PySide2.QtCore import Qt


class DispHoras(Ui_DispHoras, QWidget):     
    def __init__(self):
        super(DispHoras, self).__init__()
        self.setupUi(self)

        # Conetar os sinais com o slot
        self.ves_chbx.stateChanged.connect(self.printToTerminal)
        self.mat_chbx.stateChanged.connect(self.printToTerminal)
        self.not_chbx.stateChanged.connect(self.printToTerminal)

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
