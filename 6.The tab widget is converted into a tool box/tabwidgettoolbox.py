# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabwidgettoolbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.toolBox = QtWidgets.QToolBox(Dialog)
        self.toolBox.setGeometry(QtCore.QRect(60, 20, 261, 231))
        self.toolBox.setObjectName("toolBox")
        self.toolBoxPage1 = QtWidgets.QWidget()
        self.toolBoxPage1.setObjectName("toolBoxPage1")
        self.checkBox = QtWidgets.QCheckBox(self.toolBoxPage1)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.toolBoxPage1)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 60, 221, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.toolBoxPage1)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 90, 221, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.toolBox.addItem(self.toolBoxPage1, "")
        self.toolBoxPage2 = QtWidgets.QWidget()
        self.toolBoxPage2.setObjectName("toolBoxPage2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.toolBoxPage2)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.toolBoxPage2)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 70, 81, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.toolBoxPage2)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 110, 81, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.toolBox.addItem(self.toolBoxPage2, "")
        self.toolBoxPage3 = QtWidgets.QWidget()
        self.toolBoxPage3.setObjectName("toolBoxPage3")
        self.checkBox_7 = QtWidgets.QCheckBox(self.toolBoxPage3)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.toolBoxPage3)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.toolBoxPage3)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 100, 141, 20))
        self.checkBox_9.setObjectName("checkBox_9")
        self.toolBox.addItem(self.toolBoxPage3, "")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Chicken and chips"))
        self.checkBox_2.setText(_translate("Dialog", "Buger and chips"))
        self.checkBox_3.setText(_translate("Dialog", "Chips and russian"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), _translate("Dialog", "Food"))
        self.checkBox_4.setText(_translate("Dialog", "Coke"))
        self.checkBox_5.setText(_translate("Dialog", "Sprite"))
        self.checkBox_6.setText(_translate("Dialog", "Fanta"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), _translate("Dialog", "Drinks"))
        self.checkBox_7.setText(_translate("Dialog", "Chocolate"))
        self.checkBox_8.setText(_translate("Dialog", "Mint"))
        self.checkBox_9.setText(_translate("Dialog", "Bubble Gum"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage3), _translate("Dialog", "Ice Cream"))
