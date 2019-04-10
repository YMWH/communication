# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginSuccessfully.ui'
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
        Form.resize(947, 715)
        self.send_out = QtGui.QPushButton(Form)
        self.send_out.setGeometry(QtCore.QRect(820, 503, 112, 201))
        self.send_out.setObjectName(_fromUtf8("send_out"))
        self.giving_flower = QtGui.QCheckBox(Form)
        self.giving_flower.setGeometry(QtCore.QRect(820, 60, 105, 22))
        self.giving_flower.setObjectName(_fromUtf8("giving_flower"))
        self.giving_faeces = QtGui.QCheckBox(Form)
        self.giving_faeces.setGeometry(QtCore.QRect(820, 110, 105, 22))
        self.giving_faeces.setObjectName(_fromUtf8("giving_faeces"))
        self.giving_gold = QtGui.QCheckBox(Form)
        self.giving_gold.setGeometry(QtCore.QRect(820, 150, 105, 22))
        self.giving_gold.setObjectName(_fromUtf8("giving_gold"))
        self.giving_car = QtGui.QCheckBox(Form)
        self.giving_car.setGeometry(QtCore.QRect(820, 200, 105, 22))
        self.giving_car.setObjectName(_fromUtf8("giving_car"))
        self.giving_plane = QtGui.QCheckBox(Form)
        self.giving_plane.setGeometry(QtCore.QRect(820, 240, 105, 22))
        self.giving_plane.setObjectName(_fromUtf8("giving_plane"))
        self.giving_rocket = QtGui.QCheckBox(Form)
        self.giving_rocket.setGeometry(QtCore.QRect(820, 290, 105, 22))
        self.giving_rocket.setObjectName(_fromUtf8("giving_rocket"))
        self.giving_UFO = QtGui.QCheckBox(Form)
        self.giving_UFO.setGeometry(QtCore.QRect(820, 340, 105, 22))
        self.giving_UFO.setObjectName(_fromUtf8("giving_UFO"))
        self.giving_nice = QtGui.QCheckBox(Form)
        self.giving_nice.setGeometry(QtCore.QRect(820, 390, 105, 22))
        self.giving_nice.setObjectName(_fromUtf8("giving_nice"))
        self.gift_giving = QtGui.QPushButton(Form)
        self.gift_giving.setGeometry(QtCore.QRect(820, 440, 112, 51))
        self.gift_giving.setObjectName(_fromUtf8("gift_giving"))
        self.chat_out = QtGui.QLineEdit(Form)
        self.chat_out.setGeometry(QtCore.QRect(10, 524, 791, 171))
        self.chat_out.setObjectName(_fromUtf8("chat_out"))
        self.information_box = QtGui.QTextEdit(Form)
        self.information_box.setGeometry(QtCore.QRect(240, 40, 541, 461))
        self.information_box.setObjectName(_fromUtf8("information_box"))
        self.list_box = QtGui.QTextEdit(Form)
        self.list_box.setGeometry(QtCore.QRect(10, 40, 221, 461))
        self.list_box.setObjectName(_fromUtf8("list_box"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "讯影v1.0", None))
        self.send_out.setText(_translate("Form", "俺要说话", None))
        self.giving_flower.setText(_translate("Form", "花花", None))
        self.giving_faeces.setText(_translate("Form", "便便", None))
        self.giving_gold.setText(_translate("Form", "金条", None))
        self.giving_car.setText(_translate("Form", "跑车", None))
        self.giving_plane.setText(_translate("Form", "灰机", None))
        self.giving_rocket.setText(_translate("Form", "火箭", None))
        self.giving_UFO.setText(_translate("Form", "UFO", None))
        self.giving_nice.setText(_translate("Form", "666", None))
        self.gift_giving.setText(_translate("Form", "送礼物", None))

