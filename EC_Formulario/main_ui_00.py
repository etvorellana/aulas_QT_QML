# trabalhando com spin_combo_boxes

import sys
from PySide2.QtWidgets import QApplication, QWidget
from ui_formulario_00 import Ui_Formulario


class Formulario(Ui_Formulario, QWidget):     
    def __init__(self):
        super(Formulario, self).__init__()
        self.setupUi(self)

        self.pre1R_sbx.valueChanged.connect(self.calculaTotal)
        self.pre2R_sbx.valueChanged.connect(self.calculaTotal)
        self.pre1C_sbx.valueChanged.connect(self.calculaTotal)
        self.pre2C_sbx.valueChanged.connect(self.calculaTotal)

    def calculaTotal(self):
        """
        Calcular e exibir o preço total das spin boxes 
        e alterar o valor mostrado no QLabel
        """

        total = self.pre1R_sbx.value() + self.pre2R_sbx.value()
        total += (self.pre1C_sbx.value() / 100)
        total += (self.pre2C_sbx.value() / 100)
        self.total_lbl.setText("Total: R${}". format(str(total)))




#Executando o App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Formulario()
    window.show()
    sys.exit(app.exec_())
