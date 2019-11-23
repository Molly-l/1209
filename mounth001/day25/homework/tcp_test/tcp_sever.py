from socket import *
sockfd=socket(AF_INET,SOCK_STREAM)
sockfd.bind(('176.234.6.27',8001))
sockfd.listen(45)
while True:
    connfd,addr=sockfd.accept()
    data=connfd.recv(1024)
    if not data:
        break
    data01='fhll'
    connfd.send(data01.encode())
    connfd.close()
sockfd.close()
