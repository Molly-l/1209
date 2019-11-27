"""
epoll  方法实现IO多路服用
重点代码

【1】 创建套接字
【2】 将套接字register
【3】 创建查找字典，并维护
【4】 循环监控IO发生
【5】 处理发生的IO
"""

from socket import *
from select import *

# 创建套接字作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(3)

# 创建epoll对象
ep = epoll()

# 建立查找字典，通过IO对象的fileno找到对象
# 字典内容与关注IO保持一直{fileno:io_obj}
fdmap = {s.fileno():s}

# 关注s
ep.register(s,EPOLLIN|EPOLLERR)

# 循环监控IO的发生
while True:
    events = ep.poll()
    print("你有新的IO需要处理哦：",events)
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            # 添加新的关注对象，同时维护字典
            ep.register(c,EPOLLIN|EPOLLET) # 边缘触发
            fdmap[c.fileno()] = c
        # elif event & EPOLLIN:
        #     data = fdmap[fd].recv(1024).decode()
        #     if not data:
        #         # 客户端退出
        #         ep.unregister(fd) # 取消关注
        #         fdmap[fd].close()
        #         del fdmap[fd]
        #         continue
        #     print(data)
        #     ep.unregister(fd)
        #     ep.register(fd, POLLOUT)
        # elif event & POLLOUT:
        #     fdmap[fd].send(b'OK')
        #     ep.unregister(fd)
        #     ep.register(fd, POLLIN)


