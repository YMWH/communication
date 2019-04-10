#coding:utf-8
class A(object):
    def __init__(self, parent):
        print "A init"
        self.parent = parent

    def __del__(self):
        print "A del"

class B(object):
    def __init__(self):
        print "B init"
        self.child = A(self)
    def __del__(self):
        print "B del"


b = B()
print "func end"#函数结束对象b引用结束
print "byebye",id(b)
