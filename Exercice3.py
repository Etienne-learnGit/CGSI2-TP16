from PySide2.QtWidgets import *

class IHM(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(400,200)
        self.layout = QVBoxLayout()
        self.nb = 0

        self.button1 = QPushButton("Changer mon text !")
        self.text = QTextEdit("le nombre de clics va être affiché ici")

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.text)

        self.button1.clicked.connect(self.bouttonChange)

        self.setLayout(self.layout)

    def bouttonChange(self):
        self.nb += 1
        self.button1.setText("clic "+str(self.nb))
        self.text.setText("clic "+str(self.nb))
        return

if __name__ == "__main__":
   app = QApplication([])
   win = IHM()
   win.show()
   app.exec_()
