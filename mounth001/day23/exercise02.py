# 字节串(bytes)
# ascii编码字符串加b转换为字节串
s=b'hello world'
print(type(s))
# 字符串转换为字节串方法 :str.encode()
q='你好'
w=q.encode()
print(type(w))
# 字节串转换为字符串方法 : bytes.decode()
s=w.decode()
print(type(s))