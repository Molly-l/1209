#!/usr/bin/env python3
"""
webframe
模拟网站的后端应用行为

从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""

from socket import *
import json
from settings import *
from multiprocessing import Process
from urls import *


frame_address = (frame_ip,frame_port)

class Application:
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.bind(frame_address)
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)#程序结束，立即释放端口
    # 启动函数
    def start(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%frame_port)
        while True:
            connfd,addr = self.sockfd.accept()
            p = Process(target=self.handle,args=(connfd,))
            p.daemon = True#设置父进程退出子进程也退出，代替jion（）防止僵尸进程
            p.start()#开启进程

    # 处理具体的数据
    def handle(self,connfd):
        request = connfd.recv(1024).decode() #从httpserver接收具体请求  4
        request = json.loads(request) #请求字典,解压
        # request={'method':'GET','info':'XXXX'}      5
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info']) #response是返回的{'status': '404', 'data': 'sorry'}
            else:
                response = self.get_data(request['info'])
        elif request['method'] == 'POST':
            pass
        # 将结果返回给httpserver
        try:
            response = json.dumps(response)#打包
        except:
            connfd.close()
        else:
            connfd.send(response.encode())#将需要的数据反馈给httpserver   6
            connfd.close()

    #返回html文件内容
    def get_html(self,info):
        if info == '/':
            filename = STATIC_DIR + '/index.html' #路径
        else:
            filename = STATIC_DIR + info #浏览器输入的html文件对应本地路径
        try:
            fd = open(filename)
        except Exception:
            with open(STATIC_DIR+'/404.html') as f:
                return {'status':'404','data':f.read()}
        else:
            return {'status':'200','data':fd.read()}

    #返回非html文件内容
    def get_data(self,info):
        for url,func in urls: #从urls里面循环拿出(url,func)
            if url == info:
                return {'status':'200','data':func()}
        return {'status': '404', 'data': 'sorry'}


if __name__ == '__main__':
    app = Application()
    app.start()





