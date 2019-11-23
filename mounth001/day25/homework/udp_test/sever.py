from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd.bind(('176.234.6.27',8808))
while True:
    data01,addr=sockfd.recvfrom(1024)
    data='fhkjl;'
    sockfd.sendto(data.encode(),addr)
    print('接收到',data01.decode())


