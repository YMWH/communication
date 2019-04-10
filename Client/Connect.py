#coding:utf-8
import socket

class conNect(object):
   def __init__(self):
       # 服务器连接
       self.ip_port = ("127.0.0.1", 7889)
       self.client_socket = socket.socket()
       self.client_socket.connect(self.ip_port)

