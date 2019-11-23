# while True:
#     data=f.readline()
#     if not data:
#         break
#     print(data)

f=open('text.py','w+')
f.write('hello world')
print(f.tell())
f.seek(1,0)
data=f.read()
print(data)
f.close()
