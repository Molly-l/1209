from socket import *
#创建udp套接字
sockdf=socket(AF_INET,SOCK_DGRAM)
# server_addr=('0.0.0.0',8888)
#绑定服务地址
sockdf.bind(('0.0.0.0',8888))
#循环接受发送消息
f=open('dict.txt','r')

while True:
    #接收消息
    word,addr=sockdf.recvfrom(1024)
    for line in f:

        if line.split(' ')[0]==word.decode():
            data=line.split(' ')[1:len(line)]
    sockdf.sendto(data.encode(),addr)

    # print('Msg form %s: %s'%(addr,data.decode()))
    # f.write(data.decode())
    # sockdf.sendto(b'Thanks',addr)
sockdf.close()