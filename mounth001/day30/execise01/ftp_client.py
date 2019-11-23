"""
ftp 文件服务 ，客户端
"""
from socket import *
import sys
from time import sleep
# 服务器地址
ADDR = ('127.0.0.1',8888)


# 具体功能实现
class FtpClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd
    #获取文件列表
    def do_list(self):
        self.sockfd.send(b'L')
        data=self.sockfd.recv(128).decode()
        if data=='Ok':
            data=self.sockfd.recv(1024*1024).decode()
            print(data)
        else:
            print(data)

    # 下载文件
    def do_get(self,filename):
        # 发送请求
        self.sockfd.send(('G'+filename).encode())
        data=self.sockfd.recv(128).decode()
        if data=='OK':
            f=open(filename,'wb')
            while True:
                data=self.sockfd.recv(1024)
                if data==b'##':
                    break
                f.write(data)
            f.close()
        else:
            print(data)

    #上传
    def do_put(self,filename):
        try:
            f=open(filename,'rb')
        except Exception:
            print('文件不存在')
            return
        filename=filename.split('/')[-1]
        self.sockfd.send(('P'+filename).encode())
        data=self.sockfd.recv(128).decode()
        if data=='OK':
            while True:
                data=f.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)

