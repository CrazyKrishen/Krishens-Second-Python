import sys
from PyQt5.QtWidgets import QApplication, QDialog
from tabwidgettoolbox import Ui_Dialog

class MyForm(QDialog):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
