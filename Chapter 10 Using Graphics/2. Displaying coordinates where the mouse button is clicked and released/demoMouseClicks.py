# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMouseClicks.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(453, 317)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 431, 21))
        self.label.setObjectName("label")
        self.labelPress = QtWidgets.QLabel(Dialog)
        self.labelPress.setGeometry(QtCore.QRect(24, 65, 381, 91))
        self.labelPress.setText("")
        self.labelPress.setObjectName("labelPress")
        self.labelRelease = QtWidgets.QLabel(Dialog)
        self.labelRelease.setGeometry(QtCore.QRect(20, 160, 381, 121))
        self.labelRelease.setText("")
        self.labelRelease.setObjectName("labelRelease")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", " Displays the x,y coordinates where mouse is pressed and released"))
