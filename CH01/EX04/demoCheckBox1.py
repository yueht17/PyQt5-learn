# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(496, 447)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 511, 91))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 171, 41))
        self.label_2.setObjectName("label_2")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(0, 280, 461, 111))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 130, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxCheese = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxCheese.setObjectName("checkBoxCheese")
        self.verticalLayout.addWidget(self.checkBoxCheese)
        self.checkBoxOlives = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxOlives.setObjectName("checkBoxOlives")
        self.verticalLayout.addWidget(self.checkBoxOlives)
        self.checkBoxSausages = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxSausages.setObjectName("checkBoxSausages")
        self.verticalLayout.addWidget(self.checkBoxSausages)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Regular Pizza $10"))
        self.label_2.setText(_translate("Dialog", "select extra"))
        self.checkBoxCheese.setText(_translate("Dialog", "extra cheese"))
        self.checkBoxOlives.setText(_translate("Dialog", "extra olives"))
        self.checkBoxSausages.setText(_translate("Dialog", "extra sauages"))
