







f=open('text.py','rb')
while True:
    data=f.readline()
    if not data:
        break
    print(data)
f.close()
