from socket import *
import os
ADDR=('176.234.6.27',1234)
sockfd=socket(AF_INET,SOCK_DGRAM)
def main():
    while True:
        name = input('输入姓名')
        msg = 'L '+name
        sockfd.sendto(msg.encode(),(ADDR))
        data,addr=sockfd.recvfrom(1024)
        if data.decode()=='OK':
            print('登陆成功')
            break
    while True:
        f=os.fork()
        if f<0:
            print('创建失败')
        elif f==0:
            text = input('>>')
            if text=='quit' or text=='X':
                msg='Q '+name
                sockfd.sendto(msg.encode(), (ADDR))
                os._exit(1)
            else:
                msg = 'C ' + name +' '+text
            sockfd.sendto(msg.encode(), (ADDR))
        else:
            data, addr = sockfd.recvfrom(1024)
            if data.decode()=='子进程退出':
                os._exit(1)

            print(data.decode())




if __name__ == '__main__':
    main()
