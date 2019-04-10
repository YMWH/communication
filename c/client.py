#coding:utf-8
import communication#引入登录界面
import LoginSuccessfully#引入登录成功后的聊天界面
import sys
import json
import Connect#连接服务器
import threading#异步
from PyQt4.QtCore import *#引入pyqtSignal，便于自定义消息，并且发送给目标
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
import time
import Verification
import os

con = Connect.conNect()#连接服务器，设置为公用变量，方便页面切换时不会改变原有的连接
sign_out = None#用于接收消息的公用变量
giftarr = []


#粘包处理
def Sticky():
    print "我执行了"
    server_header = 10
    server_data = ""
    header_data = ""
    all_server = 0
    num = 0
    while True:
        if server_header <= all_server:
            server_data = json.loads(server_data)
            header_data += server_data
            break

        server_data += con.client_socket.recv(1)
        all_server = len(server_data)
    for value in server_data:
        try:
            int(value)
        except:
            num += int(server_data.find(value))
            break
    data_len = int(server_data[:num])
    data = server_data[server_header - 2:]
    while True:
        if len(data) >= data_len:
            data = json.loads(data[:data_len])
            return (header_data, data, num)
        data += con.client_socket.recv(1)

#登录界面的事件处理类
class client_sign(QThread):#发信号方用的是Qt的pyqtSignal，必须是QObject的子类或QObject
    signOut = pyqtSignal(str, int)#申请一个叫signOut的消息，该消息有一个参数，Int类型
    chatOut = pyqtSignal(str, list)
    success = pyqtSignal(str, list)
    gift = pyqtSignal(str,str)
    def __init__(self):
        super(client_sign, self).__init__()
        self.Initialization()
    #初始化
    def Initialization(self):
        self.header_len = 10
        self.data = ""
        self.data_len = 0

    #返回状态，接收数据
    def receive(self):
        global giftarr
        while True:
            print "receive启动"
            print "1111"+('threadxxx %s is running...' % threading.current_thread().name)
            self.header_data, self.data, self.num = Sticky()

            if self.header_data[self.num] == "S":
                if self.data == 1:
                    print "登录成功"
                    self.signOut.emit("S", self.data)
                elif self.data == 0:
                    print "密码错误"
                    self.signOut.emit("S", self.data)
                elif self.data == -1:
                    print "账号错误"
                    self.signOut.emit("S", self.data)
                elif self.data == 2:
                    print "重复登录"
                    self.signOut.emit("S", self.data)
            elif self.header_data[self.num] == "R":
                if self.data == 1:
                    print "注册成功"
                    self.signOut.emit("R", self.data)
                elif self.data == 0:
                    print "注册失败"
                    self.signOut.emit("R", self.data)
            elif self.header_data[self.num] == "C":
                print "C:",self.data
                self.chatOut.emit("C", self.data)
            elif self.header_data[self.num] == "N":
                print "N:", self.data
                self.success.emit("N", self.data)
            elif self.header_data[self.num] == "F":
                giftdata = ""
                data_arr = self.data[1][:]
                for index, value in enumerate(data_arr):
                    if self.data[1][index] == u"flower":
                        giftdata = u"花花"
                    elif self.data[1][index] == u"faeces":
                        giftdata = u"便便"
                    elif self.data[1][index] == u"gold":
                        giftdata = u"金条"
                    elif self.data[1][index] == u"car":
                        giftdata = u"跑车"
                    elif self.data[1][index] == u"plane":
                        giftdata = u"灰机"
                    elif self.data[1][index] == u"rocket":
                        giftdata = u"火箭"
                    elif self.data[1][index] == u"UFO":
                        giftdata = u"UFO"
                    elif self.data[1][index] == u"nice":
                        giftdata = u"666"
                    display_add = self.data[0] + u"送了一个:" + giftdata
                    self.gift.emit("F", display_add)
                    time.sleep(0.2)
    def run(self):
        self.receive()

# #礼物处理类
# class giftout(QThread):
#     def __int__(self):
#         super(giftout, self).__init__()
#     def displaygift(self, giftarr):
#         print "110" + ('threadxxx %s is running...' % threading.current_thread().name)
#         print "110",giftarr
#         arr = giftarr[:]
#         print "113",arr
#         for value in arr:
#             for key in value[1]:
#                 print "116",value[0],key
#                 value[1].remove(key)
#                 time.sleep(0.2)
#
#         print "120",arr
#         print "121",giftarr


#登录注册界面
class win(QtGui.QWidget):
    def __init__(self):
        super(win, self).__init__()
        self.url = os.path.abspath(".")
        self.url = os.path.join(self.url, "Verification/verification.png")
        print "33333" + ('threadxxx %s is running...' % threading.current_thread().name)
        self.myui = communication.Ui_Form()
        self.myui.setupUi(self)
        self.Initialization()
        self.connect(self.myui.sign, QtCore.SIGNAL('clicked()'), self.click_sign)
        self.connect(self.myui.pushButton, QtCore.SIGNAL('clicked()'), self.verificationauto)
        self.connect(self.myui.register_2, QtCore.SIGNAL('clicked()'), self.click_register)
        self.verificationauto()
    #验证码生成
    def verificationauto(self):
        self.ver_arr = Verification.auto()
        pix = QPixmap(self.url)
        self.myui.label.setPixmap(pix)
        self.ver_str = unicode("".join(self.ver_arr))
    #验证码检测
    def Testing(self):
        inputnow = unicode(self.myui.Verification_input.text())
        if inputnow == self.ver_str:
            return True
        else:
            return False
    #初始化
    def Initialization(self):
        self.header_len = 10
        self.data = ""
        self.data_len = 0
    #注册
    def click_register(self):
        if self.Testing():
            client_data = {}
            account = unicode(self.myui.account_input.text())
            password = unicode(self.myui.password_input.text())

            if account != "" or password != "":

                client_data["account"] = account
                client_data["password"] = password

                json_client = json.dumps(client_data)
                self.data_len += len(json_client)

                header_len = len(str(self.data_len))
                header_data = json.dumps(str(self.data_len) + "R" * (self.header_len - header_len - 2))
                data = header_data + json_client

                con.client_socket.sendall(data)
                self.Initialization()
            else:
                raise ValueError("Can not be empty")
        else:
            box = QtGui.QMessageBox()
            box.warning(self, u"提示", u"验证码错误", u"好的")
            self.verificationauto()
    #登录按钮,发送数据
    def click_sign(self):

        if self.Testing():
            client_data = {}

            print "1222"+('threadxxx %s is running...' % threading.current_thread().name)
            account = unicode(self.myui.account_input.text())
            password = unicode(self.myui.password_input.text())

            if account != "" or password !="":

                client_data["account"] = account
                client_data["password"] = password

                json_client = json.dumps(client_data)
                self.data_len += len(json_client)

                header_len = len(str(self.data_len))
                header_data = json.dumps(str(self.data_len) + "S" * (self.header_len - header_len - 2))
                data = header_data + json_client

                con.client_socket.sendall(data)
                self.Initialization()
            else:
                raise ValueError("Can not be empty")
        else:
            box = QtGui.QMessageBox()
            box.warning(self, u"提示", u"验证码错误", u"好的")
            self.verificationauto()
    #接收到服务器的反馈的数据进行判断检测
    def outText(self, state, num):
        if state == "S":
            if num == 1:
                box = QtGui.QMessageBox()
                box.warning(self, u"提示", u"登录成功", u"好的")
                self.close()
            elif num == 0:
                box = QtGui.QMessageBox()
                box.warning(self, u"提示", u"密码错误", u"好的")
                self.verificationauto()
            elif num == -1:
                box = QtGui.QMessageBox()
                box.warning(self, u"提示", u"无此账号，请先注册", u"好的")
                self.verificationauto()
            elif num == 2:
                box = QtGui.QMessageBox()
                box.warning(self, u"提示", u"重复登录", u"好的")
                self.verificationauto()
        elif state == "R":
            if num == 1:
                box = QtGui.QMessageBox()
                box.warning(self, u"提示", u"注册成功", u"好的")
                self.verificationauto()
            elif num == 0:
                box = QtGui.QMessageBox()
                box.warning(self, u"提示", u"此账号已经被注册过，请重新选择账号注册", u"好的")
                self.verificationauto()
#登录成功后的聊天界面
class chat(QtGui.QWidget):
    def __init__(self):
        super(chat, self).__init__()
        self.mychatui = LoginSuccessfully.Ui_Form()
        self.mychatui.setupUi(self)
        self.Initialization()
        self.check_box_arr = []
        print "192"
        self.connect(self.mychatui.send_out, QtCore.SIGNAL("clicked()"), self.send_click)
        self.connect(self.mychatui.gift_giving, QtCore.SIGNAL("clicked()"), self.check_box_send)
        self.connect(self.mychatui.giving_flower, QtCore.SIGNAL("stateChanged(int)"), self.check_box_flower)
        self.connect(self.mychatui.giving_faeces, QtCore.SIGNAL("stateChanged(int)"), self.check_box_faeces)
        self.connect(self.mychatui.giving_gold, QtCore.SIGNAL("stateChanged(int)"), self.check_box_gold)
        self.connect(self.mychatui.giving_car, QtCore.SIGNAL("stateChanged(int)"), self.check_box_car)
        self.connect(self.mychatui.giving_plane, QtCore.SIGNAL("stateChanged(int)"), self.check_box_plane)
        self.connect(self.mychatui.giving_rocket, QtCore.SIGNAL("stateChanged(int)"), self.check_box_rocket)
        self.connect(self.mychatui.giving_UFO, QtCore.SIGNAL("stateChanged(int)"), self.check_box_UFO)
        self.connect(self.mychatui.giving_nice, QtCore.SIGNAL("stateChanged(int)"), self.check_box_nice)
    #复选框，送礼物处理方法
    def check_box_flower(self, value):
        if value:
            self.check_box_arr.append("flower")
            print value
        else:
            if self.check_box_arr != []:
                self.check_box_arr.remove("flower")
    def check_box_faeces(self, value):
        if value:
            self.check_box_arr.append("faeces")
        else:
            if self.check_box_arr != []:
                self.check_box_arr.remove("faeces")
    def check_box_gold(self, value):
        if value:
            self.check_box_arr.append("gold")
        else:
            if self.check_box_arr != []:
                self.check_box_arr.remove("gold")
    def check_box_car(self, value):
        if value:
            self.check_box_arr.append("car")
        else:
            if self.check_box_arr != []:
                self.check_box_arr.remove("car")
    def check_box_plane(self, value):
        if value:
            self.check_box_arr.append("plane")
        else:
            if self.check_box_arr != []:
                self.check_box_arr.remove("plane")
    def check_box_rocket(self, value):
        if value:
            self.check_box_arr.append("rocket")
        else:
            if self.check_box_arr != []:
                self.check_box_arr.remove("rocket")
    def check_box_UFO(self, value):
        if value:
            self.check_box_arr.append("UFO")
        else:
            if self.check_box_arr != []:
                self.check_box_arr.remove("UFO")
    def check_box_nice(self, value):
        if value:
            self.check_box_arr.append("nice")
        else:
            if self.check_box_arr != []:
                self.check_box_arr.remove("nice")
    def check_box_send(self):
        check_arr = json.dumps(self.check_box_arr)
        check_arr_len = str(len(check_arr))
        length = len(check_arr_len)
        header_check = json.dumps(check_arr_len + "F" * (self.header_len - length - 2)) + check_arr
        con.client_socket.sendall(header_check)
    #登录成功后返回一个登录成功的信息
    def Success(self):
        success = json.dumps(str(True))
        success_len = len(success)
        success_data = json.dumps(str(success_len) + "T" * (self.header_len - len(str(success_len)) - 2)) + success
        con.client_socket.sendall(success_data)
    #发送聊天输入框里面的内容
    def send_click(self):
        if sign_out == 1:
            send_data = json.dumps(unicode(self.mychatui.chat_out.text()))
            if send_data != "":
                send_data_len = str(len(send_data))
                send_num_len = len(send_data_len)
                send_header = json.dumps(send_data_len + "C" * (self.header_len - send_num_len - 2))
                send_header_data = send_header + send_data
                con.client_socket.sendall(send_header_data)
                self.mychatui.chat_out.setText("")
                print "love",send_header_data
    #消息接收，第二个参数是消息里面的int参数
    def block(self, data):
        display_add = ""
        if type(data) == int:
            global sign_out#引入公用变量sign_out,以便于后续的操作
            print "1233"+('threadxxx %s is running...' % threading.current_thread().name)
            sign_out = data
            self.Success()
        else:
            if type(data) == list:
                display_add = unicode(data[0]) + unicode(":") + json.loads(data[1])
            elif type(data) == QString:
                display_add = unicode(data)
            display_data = unicode(self.mychatui.information_box.toPlainText())
            print json.dumps(display_data)
            if display_data == "":
                data = display_add
            else:
                data = display_data + "\n" + display_add
            self.mychatui.information_box.setText(data)

    #登录成功后的名字的列表
    def name_arr(self, data):
        print "227,name_arr:",data,type(data)
        name_list = ""
        for key in data:
            name_list += (key + "\n")
        self.mychatui.list_box.setText(name_list)
    def out(self):#便于打开第二页面调用，无参数
        return sign_out
    #初始化
    def Initialization(self):
        self.header_len = 10
        self.header_new_len = 0
#打开窗口
class winout(QObject):
    sOut = pyqtSignal(str, int)
    cOut = pyqtSignal(int)
    blockout = pyqtSignal(list)
    nameout = pyqtSignal(list)
    giftout = pyqtSignal(str)
    def __init__(self):
        super(winout, self).__init__()
        self.app = QtGui.QApplication(sys.argv)
        self.sign = win()
        self.chat = chat()
        self.client_sign = client_sign()
        self.client_sign.signOut.connect(self.readout)
        self.client_sign.chatOut.connect(self.readout)
        self.client_sign.success.connect(self.readout)
        self.client_sign.gift.connect(self.readout)
        self.sOut.connect(self.sign.outText)
        self.cOut.connect(self.chat.block)
        self.blockout.connect(self.chat.block)
        self.nameout.connect(self.chat.name_arr)
        self.giftout.connect(self.chat.block)

        print "22222" + ('threadxxx %s is running...' % threading.current_thread().name)
    # 登录界面启动
    def function(self):
        self.sign.show()
        self.app.exec_()

    # 聊天界面启动
    def sign_chat(self):
        self.chat.show()
        self.app.exec_()
    def readout(self, state = None, data = None):
        if state == "S":
            self.sOut.emit(state, data)
            self.cOut.emit(data)
        if state == "R":
            self.sOut.emit(state, data)
        elif state == "C":
            self.blockout.emit(data)
        elif state == "N":
            self.nameout.emit(data)
        elif state == "F":
            self.giftout.emit(data)
    def fun(self):
        self.client_sign.start()
        self.function()
        if self.chat.out() == 1:
            print "376",giftarr
            self.sign_chat()
show = winout()
show.fun()