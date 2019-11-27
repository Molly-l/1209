import re
# s='abc,fhui,jhk'
# p=r'\w{3}'
# q=re.finditer(p,s)
# for i in q:
#     print(i.group())

# s='abc'
# p=r'^ac$'
# print(re.findall(p,s))
s='k458km@kok76.com,uhuhu78@ji455.cn'
p=re.finditer('\w+@\w+\.(com|cn)',s)
for i in p:
    print(i.group())