# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XySetup.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(942, 428)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(942, 428))
        Form.setMaximumSize(QtCore.QSize(942, 428))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 271))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label_2.setObjectName("label_2")
        self.lineWidth = QtWidgets.QLineEdit(self.groupBox)
        self.lineWidth.setGeometry(QtCore.QRect(180, 20, 113, 20))
        self.lineWidth.setObjectName("lineWidth")
        self.lineHeight = QtWidgets.QLineEdit(self.groupBox)
        self.lineHeight.setGeometry(QtCore.QRect(180, 50, 113, 20))
        self.lineHeight.setObjectName("lineHeight")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 131, 16))
        self.label_4.setObjectName("label_4")
        self.motoA_CK = QtWidgets.QLabel(self.groupBox)
        self.motoA_CK.setGeometry(QtCore.QRect(180, 130, 51, 51))
        self.motoA_CK.setStyleSheet("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;")
        self.motoA_CK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-clockwise.png"))
        self.motoA_CK.setObjectName("motoA_CK")
        self.motoB_CK = QtWidgets.QLabel(self.groupBox)
        self.motoB_CK.setGeometry(QtCore.QRect(180, 190, 51, 51))
        self.motoB_CK.setStyleSheet("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;")
        self.motoB_CK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-clockwise.png"))
        self.motoB_CK.setObjectName("motoB_CK")
        self.motoA_CCK = QtWidgets.QLabel(self.groupBox)
        self.motoA_CCK.setGeometry(QtCore.QRect(270, 130, 51, 51))
        self.motoA_CCK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-anticlockwise.png"))
        self.motoA_CCK.setObjectName("motoA_CCK")
        self.motoB_CCK = QtWidgets.QLabel(self.groupBox)
        self.motoB_CCK.setGeometry(QtCore.QRect(270, 190, 51, 51))
        self.motoB_CCK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-anticlockwise.png"))
        self.motoB_CCK.setObjectName("motoB_CCK")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 24, 24))
        self.pushButton.setStyleSheet(" QPushButton {\n"
"    border-image: url(:/images/help-icon.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/help-icon-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/help-icon-click.png) 0;\n"
" }\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(170, 250, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 250, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(180, 80, 181, 16))
        self.label_8.setObjectName("label_8")
        self.slidSpeed = QtWidgets.QSlider(self.groupBox)
        self.slidSpeed.setGeometry(QtCore.QRect(180, 100, 160, 19))
        self.slidSpeed.setProperty("value", 50)
        self.slidSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.slidSpeed.setObjectName("slidSpeed")
        self.labelSpeed = QtWidgets.QLabel(self.groupBox)
        self.labelSpeed.setGeometry(QtCore.QRect(20, 100, 131, 16))
        self.labelSpeed.setObjectName("labelSpeed")
        self.btnOk = QtWidgets.QPushButton(Form)
        self.btnOk.setGeometry(QtCore.QRect(290, 290, 91, 23))
        self.btnOk.setObjectName("btnOk")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(400, 10, 571, 431))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/images/xy_setup.png"))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Xy Setups"))
        self.label.setText(_translate("Form", "Width (mm):"))
        self.label_2.setText(_translate("Form", "Height (mm):"))
        self.label_3.setText(_translate("Form", "Stepper A Directoin:"))
        self.label_4.setText(_translate("Form", "Stepper B Directoin:"))
        self.label_5.setText(_translate("Form", "ClockWise"))
        self.label_6.setText(_translate("Form", "Anti ClockWise"))
        self.label_7.setText(_translate("Form", "Limit Switch Status:"))
        self.label_8.setText(_translate("Form", "X-:0 X+:0 Y-:0 Y+:0 "))
        self.labelSpeed.setText(_translate("Form", "Speed (50%):"))
        self.btnOk.setText(_translate("Form", "Ok"))

import images_rc
