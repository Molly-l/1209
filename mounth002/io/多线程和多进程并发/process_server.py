"""
process_server.py 多进程并发模型
重点代码

创建监听套接字
循环接收客户端连接请求
当有新的客户端连接创建进程处理客户端请求
父进程继续等待其他客户端连接
当客户端退出，则对应子进程退出
"""
from socket import *
from multiprocessing import Process
import sys,signal

# 全局变量
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

# 客户端处理
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port 8888...")
while True:
    # 循环等待客户端连接
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt as e:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建线程
    p = Process(target=handle,args=(c,))
    p.daemon = True
    p.start()

