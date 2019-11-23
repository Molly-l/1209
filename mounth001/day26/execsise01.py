#http請求響應
from socket import *
#tcp服務端
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('176.234.6.27',8001))
s.listen(5)
while True:

    c,addr=s.accept()
    print('Connect from',addr)
    data=c.recv(4096).decode()
    print(data)
    if data.split(' ')[1]=='/':
        f = open('index.html', 'r')
        w01=f.read()

        html='''HTTp/1.1 200 OK
        Content-Type: text/html

        %s'''%w01
        f.close()
    else:
        html = '''HTTp/1.1 404  Not Found
               Content-Type: text/html

               Sorry..'''
    c.send(html.encode())
    c.close()
