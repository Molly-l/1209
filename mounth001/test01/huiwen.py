hw=input('输入')
# if hw[::-1]==hw:
#     print('回文')
str01=str()
# str01=hw[::-1]
# print(str01)
for i in range(len(hw)-1,-1,-1):
    str01+=hw[i]
    print(str01)
print()



