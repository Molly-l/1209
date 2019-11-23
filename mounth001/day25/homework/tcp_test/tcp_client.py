from socket import *
sockfd=socket(AF_INET,SOCK_STREAM)
sockfd.connect(('176.234.6.27',8001))
while True:
    data=input('請輸入')
    if not data:
        break
    sockfd.send(data.encode())
    mag=sockfd.recv(1024)
    print('',mag)

