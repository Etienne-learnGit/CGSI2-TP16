from PySide2.QtWidgets import *

class IHM(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(400,200)
        self.layout = QHBoxLayout()

        self.barre = QProgressBar()
        self.slider = QSlider()

        self.layout.addWidget(self.barre)
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.changeBarre)

        self.setLayout(self.layout)

    def changeBarre(self):
        r = self.slider.value()
        self.barre.setValue(r)

if __name__ == "__main__":
   app = QApplication([])
   win = IHM()
   win.show()
   app.exec_()
