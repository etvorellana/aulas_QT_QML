import sys
import random

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide2.QtCore import QUrl
 
from PySide2.QtCore import QObject, Signal, Slot

class NumberGenerator(QObject):
    def __init__(self):
        QObject.__init__(self)
    
    nextNumber = Signal(int)

    @Slot()
    def giveNumber(self):
        self.nextNumber.emit(random.randint(1, 6))


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    qmlRegisterType(NumberGenerator, 'Generators', 1, 0, 'NumberGenerator')
    
    engine.load(QUrl("exemplo_04.qml"))
    
    if not engine.rootObjects():
        sys.exit(-1)    
    
    sys.exit(app.exec_())
