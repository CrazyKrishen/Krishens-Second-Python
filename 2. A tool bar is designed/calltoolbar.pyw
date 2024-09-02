import sys

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

from toolbardemo import *



class MyForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionPlus.triggered.connect(self.plusmessage)
        self.ui.actionDivide.triggered.connect(self.dividemessage)
        self.ui.actionMultiply.triggered.connect(self.multiplymessage)
        self.ui.actionMinus.triggered.connect(self.minusmessage)

    def plusmessage(self):
        self.ui.label.setText("You selected plus")

    def dividemessage(self):
        self.ui.label.setText("You selected divide")

    def multiplymessage(self):
        self.ui.label.setText("You selected multiply")

    def minusmessage(self):
        self.ui.label.setText("You selected minus")


if __name__ =="__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
