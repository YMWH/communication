#coding:utf-8
import socket,threading
def tcplink(sock, addr):
    print "新客户端连接到来： %s:%s"%addr
    while True:
        data = sock.recv(1024)
        print data
        data = raw_input("请返回数据：")
        sock.send("hello,%s"%data)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#监听端口
s.bind(("127.0.0.1", 9991))
s.listen(5)
print "等待新的客户端连接..."
while True:
    #接受一个新的连接
    sock, addr = s.accept()  #起到一个主机作用
    #创建新的线程来处理TCP连接
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()
s.close()
