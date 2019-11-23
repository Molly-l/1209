from socket import *
#创建udp套接字
sockdf=socket(AF_INET,SOCK_DGRAM)
# server_addr=('0.0.0.0',8888)
#绑定服务地址
sockdf.bind(('0.0.0.0',8888))
#循环接受发送消息
while True:
    #接收消息
    data,addr=sockdf.recvfrom(1024)
    print('Msg form %s: %s'%(addr,data.decode()))
    sockdf.sendto(b'Thanks',addr)
sockdf.close()