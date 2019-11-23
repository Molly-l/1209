import sys

from socket import *
from multiprocessing import Process

from dict_db import User

ADDR = ('0.0.0.0',12345)
q=User("dict")
class DictServer:

    def __init__(self):
        pass
    def zhuce(self,c,name,password):
        print('l')
        if q.register(name,password):
            c.send(b"OK")
        else:
            c.send(b"f")

    def denglu(self,c,name,password):
        if q.login(name,password):
            c.send(b"OK")
        else:
            c.send(b"f")
    def do_query(self,c,name,word):
        a = q.query(word)
        if a:
            print(a[0])
            # c.send(a.encode())
            c.send(a[0].encode())
            q.insert_history(name,word)
        else:
            c.send(b'bucunz')

    def do_history(self,c,name):
        b=q.history(name)
        if b:
            list1=[]
            for i in b:
                msg = "%s   %-16s    %s"%i
                list1.append(msg)
            s='*'.join(list1)
            c.send(s.encode())
        else:
            c.send('f'.encode())




    def requset(self,c):
        while True:
            print('7')
            data=c.recv(1024*1024).decode()

            print(data)
            list01=data.split(" ")
            if list01[0]=="R":
                print('1')
                self.zhuce(c,list01[1],list01[2])
            elif list01[0]=='L':
                self.denglu(c,list01[1],list01[2])
            elif list01[0]=='Q':
                self.do_query(c,list01[1],list01[2])
            elif list01[0]=='H':
                self.do_history(c,list01[1])
            elif list01[0] == 'E':
                sys.exit()  # 退出对应的子进程

def main():
    sockdf=socket()
    sockdf.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockdf.bind(ADDR)
    sockdf.listen(5)
    print("Listen the port 8888")
    while True:
        try:
            c,iddr=sockdf.accept()
        except:
            sys.exit("服务退出")
        print('5')
        e=DictServer()
        p=Process(target=e.requset,args=(c,))
        print('4')
        p.daemon = True
        p.start()

if __name__ == '__main__':
    main()