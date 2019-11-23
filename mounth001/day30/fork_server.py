
"""
1.创建监听套接字
2.循环等待客户端链接
3.客户端链接创建新的进程为客户端服务
4.原进程继续等待其他客户端链接
5.客户端退出，对应的进程也销毁
"""
from socket import *
import os

HOST='0.0.0.0'
PoRT=8888
ADDR=(HOST,PoRT)
#
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
print()

while True:
    try:
        c,addr=s.accept()
        print('Connect from',addr)
    except KeyboardInterrupt as e:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    #创建进程
    pid=os.fork()
    if pid==0:

    elif p
