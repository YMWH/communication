# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'communication.ui'
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
        Form.resize(715, 414)
        self.sign = QtGui.QPushButton(Form)
        self.sign.setGeometry(QtCore.QRect(120, 340, 112, 51))
        self.sign.setObjectName(_fromUtf8("sign"))
        self.password_input = QtGui.QLineEdit(Form)
        self.password_input.setGeometry(QtCore.QRect(240, 180, 261, 41))
        self.password_input.setObjectName(_fromUtf8("password_input"))
        self.account_input = QtGui.QLineEdit(Form)
        self.account_input.setGeometry(QtCore.QRect(240, 100, 261, 41))
        self.account_input.setObjectName(_fromUtf8("account_input"))
        self.register_2 = QtGui.QPushButton(Form)
        self.register_2.setGeometry(QtCore.QRect(400, 340, 112, 51))
        self.register_2.setObjectName(_fromUtf8("register_2"))
        self.account = QtGui.QLabel(Form)
        self.account.setGeometry(QtCore.QRect(160, 100, 81, 51))
        self.account.setObjectName(_fromUtf8("account"))
        self.password = QtGui.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(160, 180, 81, 51))
        self.password.setObjectName(_fromUtf8("password"))
        self.Verification = QtGui.QLabel(Form)
        self.Verification.setGeometry(QtCore.QRect(160, 260, 61, 51))
        self.Verification.setObjectName(_fromUtf8("Verification"))
        self.Verification_input = QtGui.QLineEdit(Form)
        self.Verification_input.setGeometry(QtCore.QRect(240, 260, 113, 41))
        self.Verification_input.setObjectName(_fromUtf8("Verification_input"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 260, 151, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(520, 260, 151, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "讯影 v1.0", None))
        self.sign.setText(_translate("Form", "登录", None))
        self.register_2.setText(_translate("Form", "注册", None))
        self.account.setText(_translate("Form", "账号", None))
        self.password.setText(_translate("Form", "密码", None))
        self.Verification.setText(_translate("Form", "验证码", None))
        self.label.setText(_translate("Form", "Verification_img", None))
        self.pushButton.setText(_translate("Form", "看不清，换一张", None))

