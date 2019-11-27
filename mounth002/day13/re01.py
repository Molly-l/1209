import re
# 贪婪模式和非贪婪模式

# 贪婪模式
s="wooooooooooo--woo-w"
p=r'wo*'
w=re.findall(p,s)
print(w)    #['wooooooooooo', 'woo', 'w']

# 非贪婪模式
p1=r'wo*?'
w1=re.findall(p1,s)
print(w1)   #['w', 'w', 'w']


# compile()调用findall()和直接调用findall()的区别
s='Alex:1997,Sunny:1996'
pattern=r'(\w+):(\d+)'

l=re.findall(pattern,s)
print(l)#[('Alex', '1997'), ('Sunny', '1996')]

regex = re.compile(pattern) #创建一个正则表达式对象
l2=regex.findall(s)#用正则表达式对象调用findall方法
l3=regex.findall(s,0,9)

print(l2)  #[('Alex', '1997'), ('Sunny', '1996')]
print(l3)  #[('Alex', '1997')]

# finditer()的用法
s2='k458km@kok76.com,uhuhu78@ji455.cn'

pattern='\w+@\w+\.(com|cn)'

# findall()方法：如果正则表达式有子组则只能获取到子组对应的内容 ['com', 'cn']
print(re.findall(pattern,s2),'*')

# search():匹配目标字符串第一个符合内容:k458km@kok76.comp
print(re.search(pattern,s2).group())

p=re.finditer(pattern,s2)
for i in p:#finditer()的返回值是一个迭代器，需要通过for循环取出里面的内容
    print(i.group())#迭代器中存放的是match对象，需要用group()方法取出里面的内容
    #k458km@kok76.com
    #uhuhu78@ji455.cn


