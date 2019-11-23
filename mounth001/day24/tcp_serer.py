# tcp套接字服务端流程
import  socket

#创建套接字
sockfd=socket.socket(socket.AF_INET,\
            socket.SOCK_STREAM)#tcp
#绑定地址
sockfd.bind(('176.234.6.27',1234))

#设置监听
sockfd.listen(5)

#等待处理客户端连接请求
print('Waiting for connect...')
connfd,addr=sockfd.accept()
print('Connect from',addr)

#消息收发
data=connfd.recv(1024)
print('Receive',data)
n=connfd.send(b'Thanks')
print('Send %d bytes'%n)

#关闭套接字
connfd.close()
sockfd.close()