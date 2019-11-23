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

    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()
    def do_list(self):
        files=os.listdir(FTP)
        if not files:
            self.connfd.send('充值VIP,百万图书任你选'.encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        filelist=''
        for file in files:
            if file[0]!='.' and os.path.isfile(FTP+file):
                filelist+=file+'\n'
        self.connfd.send(filelist.encode())

    # 下载文件
    def do_get(self,filename):
        try:
            f=open(FTP+filename,'rb')
        except Exception:
            self.connfd.send("vip可以下载".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        while True:
            data=f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()

    # 上传
    def do_put(self, filename):
        if os.path.exists(FTP+filename):
            self.connfd.send('文件已存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
        f=open(FTP+filename,'wb')
        while True:
            data=self.connfd.recv(1024)
            if data==b'##':
                break
            f.write(data)
        f.close()
