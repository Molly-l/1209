from socket import *
import struct
ADDR=('127.0.0.1',8888)

sockfd=socket(AF_INET,SOCK_DGRAM)
st=struct.Struct()
while True:
    print('...')
    id=int(input('學號'))
    name = input('姓名').encode()
    age = int(input('年齡'))
    seroc = float(('分數'))
    data=st.pack(id,name,age,seroc)
    if not data:
        break

    sockfd.sendto(data.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print('From server:',msg.decode())
sockfd.close()