# tcp套接字客户端流程
import  socket
#创建套接字
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#请求连接
sockfd.connect(('176.234.6.27',2045))
#发送消息
n=sockfd.send('yuio'.encode())
#接收消息
data=sockfd.recv(1024)
print(data.decode())
#关闭套接字
sockfd.close()
