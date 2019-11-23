'''（r文件不存在报错，w,a会新建）w清空重写，a追加'''

f=open('w01.txt','ab')
# f.write('111')
bytes1='dfyt'.encode()#字符串转换二进制
f.write(bytes1)

f.close()
