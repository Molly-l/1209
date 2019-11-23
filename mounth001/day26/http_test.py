#http請求響應
from socket import *
#tcp服務端
s=socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('176.234.6.27',8002))
s.listen(5)
c,addr=s.accept()

print('Connect from',addr)

data=c.recv(4096).decode()
print(data)

html='''HTTp/1.1 200 OK
Content-Type: text/html

Hello world'''
c.send(html.encode())
c.close()
s.close()