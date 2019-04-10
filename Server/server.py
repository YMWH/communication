#coding:utf-8
import socket
import json
import threading
import os
from PyQt4.QtCore import *

# 创建锁
mutex = threading.Lock()
lock = threading.Lock()
lock2 = threading.Lock()

# 创建读取文本数据的储存的公用变量
data_naw = []
data_str = ""

#记录客户端登录成功后的套接字和用户名，格式是2维数组：[["套接字0", "用户名0"], ["套接字1", "用户名1"]]
on_line = []

# 相对路径
url = os.path.abspath(".")
url = os.path.join(url, "data.txt")

client_arr = []#记录客户端套接字
sign_arr = []#记录登录成功的客户端的用户名

# 创建套接字
sv_socket = socket.socket()
sv_socket.bind(("127.0.0.1", 7889))
sv_socket.listen(5)

# 打开文本操作储存数据，账号已经密码
def writfil(data):
    f = open(url, "w")
    json.dump(data, f)
    f.close()
def openfil():
    global data_naw, data_str
    f = open(url, "r")
    while True:
        data = f.read(10)
        data_str += data
        if not data:
            if data_str != "":
                data_naw = json.loads(data_str)
                data_str = ""
            f.close()
            break
try:
    openfil()
except:
    f = open(url, "w")
    f.close()


class server(QObject):
    out = pyqtSignal(int)
    wri = pyqtSignal(list)
    def __init__(self):
        super(server, self).__init__()


    #接收数据，沾包处理
    def receive(self, server_socket, addr):
        print "欢迎客户端：%s:%s" %addr
        print "2222",('threadxxx %s is running...' % threading.current_thread().name)
        while True:
            self.header_len = 10
            self.data = ""
            self.header_now_len = 0
            self.status = -1#-1代表登录失败（账号错误），0代表密码错误，1代表登录成功
            while True:
                if self.header_now_len >= self.header_len:
                    break
                else:
                    #客户端那边异常关闭，错误处理以及关闭该错误的套接字和删除客户端的登录信息
                    try:
                        self.data += server_socket.recv(1)
                    except:
                        # 加锁
                        lock.acquire(True)
                        for value in on_line:
                            if value[0] == server_socket:
                                sign_arr.remove(value[1])
                                on_line.remove(value)
                                break
                        for key in client_arr:
                            if key == server_socket:
                                client_arr.remove(key)
                                break
                        # 解锁
                        lock.release()
                        names = json.dumps(sign_arr)
                        names_len = len(names)
                        names_data = json.dumps(str(names_len) + "N" * (10 - len(str(names_len)) - 2)) + names
                        self.sendout(names_data)
                        server_socket.close()
                        exit()

                    self.header_now_len = len(self.data)
            # 容易报错位置，ValueError: No JSON object could be decoded
            header_data = json.loads(self.data)

            if header_data.find("S") != -1:
                # "S"代表登录状态
                self.inrecv(header_data, server_socket, "S", addr)
            elif header_data.find("R") != -1:
                #"R"代表注册状态
                self.inrecv(header_data, server_socket, "R", addr)
            elif header_data.find("C") != -1:
                # "C"代表聊天状态
                self.inrecv(header_data, server_socket, "C", addr)
            elif header_data.find("T") != -1:
                # "T"代表名字的列表，后面会换成"N"
                self.inrecv(header_data, server_socket, "T", addr)
            elif header_data.find("F") != -1:
                # "F"代表送礼物
                self.inrecv(header_data, server_socket, "F", addr)
    # 包头处理
    def inrecv(self, header_data, server_socket, state, addr):
        index = header_data.find(state)
        send_data_len = int(header_data[:index])
        data = header_data[self.header_len:]
        while True:
            if len(data) >= send_data_len:
                self.Handle(data, self.status, server_socket, state, addr)
                break
            else:
                data += server_socket.recv(1024)
    #数据处理,alldata:要用的数据，status:默认状态为-1，与登录有关，server_socket:子线程套接字,state:状态标识，addr:客户端ip，暂时无用
    def Handle(self, alldata, status, server_socket, state, addr):
        client_header = 10
        client_data_len = 0
        data = json.loads(alldata)
        data_list = unicode(data)
        data_list_start = data_list.find("\'")
        data_list_end = data_list.find(",")
        data_account = data_list[data_list_start:data_list_end]

        if state == "S":
            lock2.acquire(True)

            for num in range(len(data_naw)):
                data = data_naw[num]
                dec_list = str(data)
                dec_list_start = dec_list.find("\'")
                dec_list_end = dec_list.find(",")
                dec_account = dec_list[dec_list_start:dec_list_end]
                if dec_list == data_list:
                    if on_line == []:
                        status = 1
                        on_line.append([server_socket, data["account"]])
                    else:
                        for value in on_line:
                            print "146:",data["account"],type(data["account"])
                            print "147:",value[1],type(value[1])
                            if value[1] != data["account"]:
                                status = 1
                                on_line.append([server_socket, data["account"]])
                                break
                            else:
                                status = 2
                                break
                else:
                    if status != 2:
                        if data_account == dec_account:
                            status = 0
                            break
                        else:
                            status = -1
                if status == 1:
                    sign_arr.append(data["account"])
                    break
            if status == -1:
                client_header = 11

            lock2.release()
            status_data = json.dumps(status)
            client_data_len += len(status_data)
            client_data_h = json.dumps(str(client_data_len) + state * (client_header - client_data_len - 2)) + status_data
            client_arr[len(client_arr) - 1].sendall(client_data_h)
        if state == "R":
            mutex.acquire(True)
            length = len(data_naw)

            for num in range(len(data_naw)):
                if data_naw[num][u"account"] == data[u"account"]:
                    status = 0
                    break
                else:
                    if num == len(data_naw) - 1:
                        data_naw.append(data)
                        status = 1

            if length == 0:
                data_naw.append(data)
                status = 1
            if status == 1:
                self.out.connect(openfil)
                self.wri.connect(writfil)
                self.wri.emit(data_naw)
                self.out.emit(1)
            mutex.release()
            status = json.dumps(status)
            client_data_len += len(status)
            client_data_h = json.dumps(str(client_data_len) + state * (client_header - client_data_len - 2)) + status
            client_arr[len(client_arr)-1].sendall(client_data_h)
        if state == "T":
            names = json.dumps(sign_arr)
            names_len = len(names)
            names_data = json.dumps(str(names_len) + "N" * (client_header - len(str(names_len)) - 2)) + names
            self.sendout(names_data)
        if state == "C":
            name = ""
            for key in on_line:
                if key[0] == server_socket:
                    name += key[1]
                    break
            cdata = json.dumps([name, alldata])
            chatdata_len = len(cdata)
            chatdata = json.dumps(str(chatdata_len) + "C" * (client_header - len(str(chatdata_len)) - 2)) + cdata
            self.sendout(chatdata)
        if state == "F":
            #实现发送的数据是"24FFFFFF"["用户名", ["礼物1","礼物2"]]
            gift = []
            for value in on_line:
                if value[0] == server_socket:
                    gift.append(value[1])
                    gift.append(data)
            gift_data = json.dumps(gift)
            gift_len = len(gift_data)
            gift_len_str = str(gift_len)
            length = len(gift_len_str)
            header_gift = json.dumps(gift_len_str + "F" * (client_header - length - 2)) + gift_data
            self.sendout(header_gift)

    # 发送给各个登录成功后的客户端
    def sendout(self, alldata):
        for value in client_arr:
            value.sendall(alldata)

fun = server()
#多线程
def thread():
    while True:
        server_socket, addr = sv_socket.accept()
        client_arr.append(server_socket)
        t = threading.Thread(target=fun.receive, args=(server_socket, addr))
        t.start()
thread()