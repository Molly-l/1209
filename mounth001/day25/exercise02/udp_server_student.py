from socket import *
#创建udp套接字
sockdf=socket(AF_INET,SOCK_DGRAM)
# server_addr=('0.0.0.0',8888)
#绑定服务地址
sockdf.bind(('0.0.0.0',8888))
#循环接受发送消息
f=open('1.txt','a')

while True:
    #接收消息
    student,addr=sockdf.recvfrom(1024)

    # print('Msg form %s: %s'%(addr,data.decode()))
    # f.write(data.decode())
    # sockdf.sendto(b'Thanks',addr)
sockdf.close()