import re

s='Alex:1997,Sunny:1996'
s1='jim,i'
pattern=r'(\w+):(\d+)'

l=re.findall(pattern,s)
print(l)
#
regex = re.compile(pattern)
l=regex.findall(s,9)
print(l)
# l2=regex.findall(s1)

# l=re.findall(pattern,s)

# print(l)
#正则表达式内容切割字符串
l=re.split(r',',s)
print(l)
#替换目标字符串
s=re.sub(r':','--',s)
print(s)