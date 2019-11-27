msg=int(input('输入字符串'))
print('第一个字符是%s'%msg[0])
print('倒数第二个字符是%s'%msg[-2])
print('前两个字符是%s'%msg[:2])
print('倒序打印所有%s'%msg[::-1])
print(msg[1::2])
print()
count=0
for i in msg:
    count+=1
print(count)

length=len(msg)
if length%2:
    print(msg[length//2])
    