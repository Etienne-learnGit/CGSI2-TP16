from PySide2.QtWidgets import *

class calculator(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Calculator")
        self.setMinimumSize(400,200)
        self.nb = ""

        self.layoutV = QVBoxLayout()
        self.layoutH = QHBoxLayout()
        self.layoutVF1 = QVBoxLayout()
        self.layoutVF2 = QVBoxLayout()
        self.layoutH1 = QHBoxLayout()
        self.layoutH2 = QHBoxLayout()
        self.layoutV1 = QVBoxLayout()
        self.layoutV2 = QVBoxLayout()
        self.layoutV3 = QVBoxLayout()
        self.layoutV4 = QVBoxLayout()

        self.text = QTextEdit("0")
        self.text.setMaximumHeight(30)
        self.buttonC = QPushButton("C")
        self.B7 = QPushButton("7")
        self.B4 = QPushButton("4")
        self.B1 = QPushButton("1")
        self.B0 = QPushButton("0")
        self.B8 = QPushButton("8")
        self.B5 = QPushButton("5")
        self.B2 = QPushButton("2")
        self.Bvirgule = QPushButton(",")
        self.buttonCE = QPushButton("CE")
        self.B9 = QPushButton("9")
        self.B6 = QPushButton("6")
        self.B3 = QPushButton("3")
        self.Begal = QPushButton("=")
        self.Bdiv = QPushButton("/")
        self.Bmul = QPushButton("*")
        self.Bmoins = QPushButton("-")
        self.Bplus = QPushButton("+")

        self.layoutV1.addWidget(self.B7)
        self.layoutV1.addWidget(self.B4)
        self.layoutV1.addWidget(self.B1)
        self.layoutV1.addWidget(self.B0)
        self.layoutH1.addLayout(self.layoutV1)
        self.layoutV2.addWidget(self.B8)
        self.layoutV2.addWidget(self.B5)
        self.layoutV2.addWidget(self.B2)
        self.layoutV2.addWidget(self.Bvirgule)
        self.layoutH1.addLayout(self.layoutV2)
        self.layoutV3.addWidget(self.B9)
        self.layoutV3.addWidget(self.B6)
        self.layoutV3.addWidget(self.B3)
        self.layoutV3.addWidget(self.Begal)
        self.layoutH2.addLayout(self.layoutV3)
        self.layoutV4.addWidget(self.Bdiv)
        self.layoutV4.addWidget(self.Bmul)
        self.layoutV4.addWidget(self.Bmoins)
        self.layoutV4.addWidget(self.Bplus)
        self.layoutH2.addLayout(self.layoutV4)

        self.layoutVF1.addWidget(self.buttonC)
        self.layoutVF1.addLayout(self.layoutH1)
        self.layoutVF2.addWidget(self.buttonCE)
        self.layoutVF2.addLayout(self.layoutH2)

        self.layoutH.addLayout(self.layoutVF1)
        self.layoutH.addLayout(self.layoutVF2)

        self.layoutV.addWidget(self.text)
        self.layoutV.addLayout(self.layoutH)

        self.B7.clicked.connect(self.operation7)
        self.B4.clicked.connect(self.operation4)
        self.B1.clicked.connect(self.operation1)
        self.B0.clicked.connect(self.operation0)
        self.B8.clicked.connect(self.operation8)
        self.B5.clicked.connect(self.operation5)
        self.B2.clicked.connect(self.operation2)
        self.Bvirgule.clicked.connect(self.operationvirgule)
        self.B9.clicked.connect(self.operation9)
        self.B6.clicked.connect(self.operation6)
        self.B3.clicked.connect(self.operation3)
        self.Bdiv.clicked.connect(self.operationdiv)
        self.Bmul.clicked.connect(self.operationmul)
        self.Bmoins.clicked.connect(self.operationmoins)
        self.Bplus.clicked.connect(self.operationplus)

        self.Begal.clicked.connect(self.realiseOperation)
        self.buttonCE.clicked.connect(self.CE)
        self.buttonC.clicked.connect(self.C)

        self.setLayout(self.layoutV)

    def operation7(self):
        self.nb += str(self.B7.text())
        self.text.setText(self.nb)
        return
    def operation4(self):
        self.nb += str(self.B4.text())
        self.text.setText(self.nb)
        return
    def operation1(self):
        self.nb += str(self.B1.text())
        self.text.setText(self.nb)
        return
    def operation0(self):
        self.nb += str(self.B0.text())
        self.text.setText(self.nb)
        return
    def operation8(self):
        self.nb += str(self.B8.text())
        self.text.setText(self.nb)
        return
    def operation5(self):
        self.nb += str(self.B5.text())
        self.text.setText(self.nb)
        return
    def operation2(self):
        self.nb += str(self.B2.text())
        self.text.setText(self.nb)
        return
    def operationvirgule(self):
        self.nb += str(self.Bvirgule.text())
        self.text.setText(self.nb)
        return
    def operation9(self):
        self.nb += str(self.B9.text())
        self.text.setText(self.nb)
        return
    def operation6(self):
        self.nb += str(self.B6.text())
        self.text.setText(self.nb)
        return
    def operation3(self):
        self.nb += str(self.B3.text())
        self.text.setText(self.nb)
        return
    def operationdiv(self):
        self.nb += str(self.Bdiv.text())
        self.text.setText(self.nb)
        return
    def operationmul(self):
        self.nb += str(self.Bmul.text())
        self.text.setText(self.nb)
        return
    def operationmoins(self):
        self.nb += str(self.Bmoins.text())
        self.text.setText(self.nb)
        return
    def operationplus(self):
        self.nb += str(self.Bplus.text())
        self.text.setText(self.nb)
        return
    def realiseOperation(self):
        self.nb = str(eval(self.nb))
        self.text.setText(self.nb)
        return
    def CE(self):
        if self.nb.isdigit() == True :
            self.nb = ""
            self.text.setText("0")
            return
        else :
            lst = []
            for i in range(len(self.nb)) :
                lst.append(self.nb[i])
            lst = lst[:len(lst)-1]
            self.nb = "".join(lst)
            self.text.setText(self.nb)
        return
    def C(self):
        self.nb = ""
        self.text.setText("0")
        return

if __name__ == "__main__":
   app = QApplication([])
   win = calculator()
   win.show()
   app.exec_()
