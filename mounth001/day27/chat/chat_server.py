from socket import *

user={}
ADDR=('176.234.6.27',1234)
sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd.bind((ADDR))

def main():
    while True:
        data,addr = sockfd.recvfrom(1024)
        data01=data.decode().split(' ')
        if data01[0]=='L':
            if data01[1] in user:
                sockfd.sendto('用户名存在'.encode(),addr)
                return
            else:
                sockfd.sendto(b'OK',addr)
                for i in user:
                    n=data01[1]+'进入了聊天室'
                    print(user[i])
                    sockfd.sendto(n.encode(),user[i])
                user[data01[1]]=addr
            print()
        elif data01[0]=='C':
            m=data01[1]+':'+' '.join(data01[2:])
            for i in user:
                sockfd.sendto(m.encode(),user[i])
        elif data01[0]=='Q':
            del user[data01[1]]
            sockfd.sendto('子进程退出'.encode(), addr)

            m=data01[1]+'退出了聊天室'
            for i in user:
                sockfd.sendto(m.encode(),user[i])
    # print(data.decode())
if __name__ == '__main__':
    main()

