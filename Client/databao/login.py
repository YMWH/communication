# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        Form.setStyleSheet(_fromUtf8(""))
        self.labe_lname = QtGui.QLabel(Form)
        self.labe_lname.setGeometry(QtCore.QRect(100, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labe_lname.setFont(font)
        self.labe_lname.setStyleSheet(_fromUtf8("border-color: rgb(85, 85, 255);"))
        self.labe_lname.setObjectName(_fromUtf8("labe_lname"))
        self.label_password = QtGui.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(100, 100, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet(_fromUtf8("border-color: rgb(255, 85, 255);"))
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.pushButton_login = QtGui.QPushButton(Form)
        self.pushButton_login.setGeometry(QtCore.QRect(130, 180, 81, 31))
        self.pushButton_login.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);"))
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        self.pushButton_register = QtGui.QPushButton(Form)
        self.pushButton_register.setGeometry(QtCore.QRect(230, 180, 81, 31))
        self.pushButton_register.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);"))
        self.pushButton_register.setObjectName(_fromUtf8("pushButton_register"))
        self.lineEdit_name = QtGui.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(180, 50, 131, 31))
        self.lineEdit_name.setStyleSheet(_fromUtf8("border-color: rgb(255, 255, 0);"))
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.lineEdit_password = QtGui.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(180, 100, 131, 31))
        self.lineEdit_password.setStyleSheet(_fromUtf8("border-color: rgb(255, 255, 0);"))
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Mychat", None))
        self.labe_lname.setText(_translate("Form", "用户名：", None))
        self.label_password.setText(_translate("Form", "密  码：", None))
        self.pushButton_login.setText(_translate("Form", "登录", None))
        self.pushButton_register.setText(_translate("Form", "注册", None))

