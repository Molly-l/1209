# 2. 编写一个程序，将下面的字符串的各个单词的字母顺序\
# 翻转形成新的字符串（注：原单词顺序保持不变）
# “welcome to beijing"，
# 将变成"emoclew ot gnijieb"。
str01='welcome to beijing'
list01=str01.split(' ')
# list02=[]
# for i in range(len(list01)):
#     list01[i]=list01[i][::-1]

for i in list01:
    i=i[::-1]

# print(list01)
str01=' '.join(list01)
print(str01)

