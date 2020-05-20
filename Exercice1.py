from PySide2.QtWidgets import *
from random import *

class IHM(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")
        self.setMinimumSize(500,300)
        self.layout = QVBoxLayout()

        self.label = QLabel("CSI")
        self.button1 = QPushButton("Changer de cycle")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button1)

        self.button1.clicked.connect(self.buttonClick)

        self.setLayout(self.layout)

    def buttonClick(self):
        lst = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        r = randint(0, 5)
        self.label.setText(lst[r])

if __name__ == "__main__":
   app = QApplication([])
   win = IHM()
   win.show()
   app.exec_()
