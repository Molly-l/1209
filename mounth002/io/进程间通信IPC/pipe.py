"""
pipe.py 管道通信

注意： 管道对象需在父进程中创建，子进程从父进程中获取
"""

from multiprocessing import Process,Pipe

# 创建管道
# False单向管道 fd1->recv  fd2->send
# 不要在一个进程中同时使用fd1 fd2
fd1,fd2 = Pipe(False)

def app1():
    print("启动app1,请登录，（可以使用app2）")
    print("向app2发请求")
    fd1.send("app1需要：用户名，头像") # 写管道
    data = fd1.recv()
    print("Oh yeah",data)

def app2():
    data = fd2.recv() # 读管道
    print("app1请求:",data)
    fd2.send({'name':'Han','image':'有'})

p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()
