import gevent
from gevent import monkey
monkey.patch_all()
from socket import *

def handle(c):
    while True:
        data=c.recv(1024).decode()
        if not data:
            return
            print(data)
            c.send(b'OK')
#创建套接字
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
#
while True:
    c,addr=s.accept()
    print('Connect from',addr)

    gevent.spawn(handle,c)
