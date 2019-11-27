#!/usr/bin/env python3
"""
httpserver 3.0
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""


from socket import *
import sys
from threading import Thread
from config import *
import re
import json

# 和frame进行交互
def connect_frame(env):
    s = socket()
    try:
        # 链接webframe
        s.connect((frame_ip,frame_port))
    except:
        return
    data = json.dumps(env) # 转换为json,打包
    s.send(data.encode())#将请求发送给WebFrame  3

    data = s.recv(1024*1024*10).decode()#从WebFrame接收反馈数据   7
    try:
        data = json.loads(data) # {‘status’:200,'data':'c'}解压
        return data
    except:
        return #不写就返回空的

class HTTPServer:
    def __init__(self):
        self.host = host
        self.port = port
        self.address = (host,port)
        # 创建套接字
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               DEBUG)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            client = Thread(target=self.handle,
                            args = (connfd,))
            client.setDaemon(True)#设置父线程退出子线程也退出，代替jion（）防止僵尸线程
            client.start()#开启线程

    # 具体处理客户端请求
    def handle(self,connfd):
        request = connfd.recv(4096).decode()#获取客户端http请求 1
        print(request)
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern,request).groupdict()#解析http请求  2
        except:
            connfd.close()
            return
        else:
            # 和frame进行交互
            response = connect_frame(env) #调用函数的返回值
            if response:#不为空
                self.send_response(connfd,response)

    # 组织http响应，发送给浏览器
    def send_response(self,connfd,response):
        # response={'status':'200','data':'ccc'}
        if response['status'] == '200':
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type:text/html\r\n"
            data += '\r\n'
            data += response['data']
        elif response['status'] == '404':
            data = "HTTP/1.1 404 Not Found\r\n"
            data += "Content-Type:text/html\r\n"
            data += '\r\n'
            data += response['data']
        elif response['status'] == '500':
            pass
        connfd.send(data.encode())#将数据组织为Response格式发送给客户端(浏览器)   8

if __name__ == '__main__':
    httpd = HTTPServer()
    httpd.server_forever() # 启动服务












