f=open("w01.txt",'rb')
# e=f.read()
# print(e)
# b'111\nfujhk dfyt'


e=f.read()
print(e.decode())#二进制转字符串decode()

f.close()