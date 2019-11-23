from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
while True:
    data=input('請輸入')
    if not data:
        break
    sockfd.sendto(data.encode(),('176.234.6.27',8808))
    mag,addr=sockfd.recvfrom(1024)
    print('接收到',mag.decode())
sockfd.close()

