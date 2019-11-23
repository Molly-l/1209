import sys
from socket import socket
ADDR = ('0.0.0.0',12345)

class DictClient:

    def __init__(self,sockdf):
        self.sockdf=sockdf
    def zhuce(self,name,password):
        message="R %s %s"%(name,password)
        print(message)
        self.sockdf.send(message.encode())
        data01=self.sockdf.recv(1024).decode()
        if data01=='OK':
            print('成功')
        elif data01=="f":
            print('失败')
    def denglu(self,name,password):
        message = "L %s %s" % (name, password)
        self.sockdf.send(message.encode())
        data01 = self.sockdf.recv(1024).decode()
        if data01 == 'OK':
            print('成功')
            return True
        elif data01 == "f":
            print('失败')
    def do_query(self,name):
        word=input('输入单词：')
        message = "Q %s %s" % (name,word)
        self.sockdf.send(message.encode())
        data01 = self.sockdf.recv(1024).decode()
        if data01=='bucunz':
            print('不存在')
        else:
            print(data01)


    def do_history(self,name):
        message = "H %s" % name
        self.sockdf.send(message.encode())
        data01 = self.sockdf.recv(1024).decode()
        if data01=="f":
            print('没记录')
        else:
            c=data01.split('*')
            for i in c:
                print(i)
def login(name,find):
    while True:
        print("""
                ==============%s Query ============
                  1.查单词     2.历史记录     3.注销
                ===================================
                """ % name)
        cmd=input('输入选项')
        if cmd=="1":
            find.do_query(name)
        elif cmd=="2":
            find.do_history(name)
        elif cmd=="3":
            return
        else:
            print('输入正确的')


def main():
    sockdf=socket()
    # try:
    sockdf.connect(ADDR)
    # except Exception as e:
    #     print(e)
    #     return
    find=DictClient(sockdf)
    while True:
        print("""
        ========== Welcome ============
         1.注册     2.登录     3.退出
       ===============================
       """)
        cmd = input("选项(1,2,3):")
        if cmd=="1":
            name=input("名字")
            password=input("密码")
            find.zhuce(name,password)
        elif cmd=="2":
            name = input("名字")
            password = input("密码")

            if find.denglu(name,password):
                login(name,find)

        elif cmd=="3":
            sockdf.send(b"E")
            sys.exit("谢谢使用")


if __name__ == '__main__':
    main()