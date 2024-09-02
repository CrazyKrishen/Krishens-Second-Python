import sys
from PyQt5.QtWidgets import QApplication, QDialog
from tabwidgetdemo import Ui_Dialog

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


#Note that here you dont have add all other fucntions like box is checked etc... even though you added it on the .ui file
#The pyuic5 converts the .ui into an .py and implements its own code inside the .py once its converted. So you convert the .ui normall like you usually do.
#Here you  just create the structure of self.ui and the main function
