# tcp套接字服务端流程
import  socket
#创建套接字
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定服务地址和端口号
sockfd.bind(('176.234.6.27',2045))
#监听
sockfd.listen()
#等待处理客户端请求
# accept是一个阻塞语句，如果没有收到客户端请求，后面语句将不会执行
connfd,addr=sockfd.accept()
print(addr)
data=connfd.recv(1024)#参数为数据大小
print(data.decode())
# 接受客户端发送的数据
data01=b'ghjl'
#向客户端发送数据
n=connfd.send(data01)
#关闭套接字
sockfd.close()


