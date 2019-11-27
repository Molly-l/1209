"""
ftp 文件服务器 服务端
多进程/多线程并发 socket
"""
from socket import *
from threading import Thread
import sys,os
from time import sleep

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
FTP = "/home/tarena/FTP/" # 文件库位置

# 实现具体功能
class FtpServer(Thread):
    """
    查看文件列表，上传，下载，退出
    """
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    # 获取文件列表
    def do_list(self):
        files = os.listdir(FTP)#获取路径下的所有文件名列表    3
        if not files:
            self.connfd.send("文件名不存在或路径错误".encode())  #4
            return
        else:
            self.connfd.send(b'OK')  #4
            sleep(0.1)

        filelist = ""
        for file in files:
            if file[0] == '.' and \
                    os.path.isfile(FTP+file):#os.path.isfile()判断某一路径是否为目录
                #如果是隐藏文件（.）或者是目录则不添加
                continue
            filelist += file + '\n'
        self.connfd.send(filelist.encode())   #6

        # for file in files:
        #     # 不是隐藏文件并且是普通文件
        #     if file[0] != '.' and \
        #             os.path.isfile(FTP+file):
        #         sleep(0.1)
        #         self.connfd.send(file.encode())
        # sleep(0.1)
        # self.connfd.send(b'##')

    # 下载文件（上传给客户端）
    def do_get(self,filename):
        try:
            f = open(FTP+filename,'rb')
        except Exception:

            self.connfd.send("文件不存在".encode())# 文件不存在  10
            return
        else:
            self.connfd.send(b'OK')   #10
            sleep(0.1)

        while True: #发送文件  12
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()

    # 上传
    def do_put(self,filename):
        if os.path.exists(FTP+filename):#判断文件是否存在
            self.connfd.send('文件已存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接收文件
        f = open(FTP+filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    # 分配任务
    def run(self):
        while True:

            data=self.connfd.recv(1024).decode()# 接收客户端请求  2  9
            # 判断请求类型
            if not data or data == 'Q':#如果客户端断开连接，则会向服务端发送（空字符）
                return # 线程结束
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)

# 搭建网络并发模型
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    print("Listen the port 8888...")
    while True:
        # 循环等待客户端连接
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt as e:
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建线程
        t = FtpServer(c)
        t.setDaemon(True)#父线程退出，子线程也退出，不用再写jion()
        t.start()#开启线程，相当于调用线程类中run（）方法

if __name__ == '__main__':
   main()