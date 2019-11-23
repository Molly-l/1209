from socket import *
from select import select

#创建监听套接字
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind('176.234.6.27',8001)
s.listen(3)
#设置关注列表
rlist=[s]#等待客户端连接
wlist=[]
xlist=[]
#监控IO发生
while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            #有客户端链接
            c,addr=r.accept()
            print('Connect from',addr)
            rlist.append(c)#链接对象加入监控
        else:
            data=r.recv(1024).decode()
            if not data:
                rlist.remove(r)#移除链接对象
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r)
    for w in ws:
        w.send(b'OK')
        wlist.remove(w)#从写监控中移除