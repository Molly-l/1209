
"""
1.创建监听套接字
2.循环等待客户端链接
3.客户端链接创建新的线程客户端服务
4.原线程继续等待其他客户端链接
5.客户端退出，对应的线程也退出
"""
from socket import *
import os

HOST='0.0.0.0'
PoRT=8888
ADDR=(HOST,PoRT)