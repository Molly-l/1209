from socket import *

# 创建tcp套接字
sockfd = socket() # 默认值

# 连接服务器
server_addr = ('127.0.0.1',8888) # 服务器地址
sockfd.connect(server_addr)

# 先发后收
while True:
    msg = input("Msg:")
    if not msg:
        break
    sockfd.send(msg.encode()) #字节串
    data = sockfd.recv(1024)
    print("From server:",data.decode())

sockfd.close()









