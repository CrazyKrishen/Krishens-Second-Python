import sys
from PyQt5 import QtWidgets, QtCore
from tabwidgetstacked import Ui_Dialog

class MyForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("Food")
        self.ui.comboBox.addItem("Drinks")
        self.ui.comboBox.addItem("Ice Cream")
        self.ui.comboBox.activated[int].connect(self.ui.stackedWidget.setCurrentIndex)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
        
#here you have to define a bit of code besides just creating the self.ui but the main code is still in the .py.
#This is becuase we use a comboBox which is not part of the tabs, its an extra feature for selecting the category you want to choose
#But the tabs code is still coded automatically in the .py file when you convert the .ui to .py

#But when you convert the tabs into a toolBox, theres no need to code extra, just the self.ui here becuase
#toolBox is still within tabs box not outside of the tab.
