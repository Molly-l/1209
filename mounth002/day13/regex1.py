import re
s='热烈庆祝达内17周年，2002年，学生60万＋'
pattern=r'\d+'
#返回迭代对象
it=re.finditer(pattern,s)
# print(it)
#每个match对象只匹配一个
for i in it:

    print(i.group())#获取match对象匹配内容

#完全匹配
obj=re.fullmatch('\w+',s)
print(obj)