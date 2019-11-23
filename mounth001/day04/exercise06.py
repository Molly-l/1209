# str01=input('输入一个字符串')
# for chr01 in str01:
#     print(chr01)
#     print(ord(chr01))
# '''for chr01 in range(12)'''

while True:
    bianmazhi=input('输入编码值')
    if bianmazhi=='':
        break
    print(chr(int(bianmazhi)))
