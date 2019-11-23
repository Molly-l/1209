# l01=[0,1,2,3]
# l01.remove(1)
# print(l01)
#
# del l01[3]
# print(l01)


# list=['水金地火木土','天王','海王']
# print('距离太阳最近的行星%s,距离太阳最远的行星%s'%list[])

# list01=[]
# while True:
#     name=input('输入学生姓名')
#     if name:
#         list01.append(name)
#     else:
#         break
#
# print(list01)

# list_02=[]
# zongchengji=0
# while True:
#     chengji=input('输入学生成绩')
#     if chengji=='':
#         break
#     else:
#         list_02.append(int(chengji))
#         # zongchengji+=int(chengji)
#
# print('输出最高分%.1f,输出最低分%.1f,和平均分%.1f'%
#       (max(list_02),min(list_02),sum(list_02)/
#        len(list_02)))
# i=0
# i=1
#
# list01=[3,45,8,12,36,7,3]
# list02=[]
# for i in list01:
#     if list01>10:
#         list02.append(i)
# print(list02)
#
# max_num=list02[0]
# list01=[3,45,8,12,36,7,3]
# for i in list01:
#     if i>max_num:
#         max_num=i
# print(max_num)
# list01[::-1]

# for i in range(len(list01)-1,-1,-1):
#     if list01[i]%2:
#         del list01[i]
# print(list01)

yingwen='How are you'
list01=yingwen.split(' ')

list02=list01[::-1]

yingwen01=' '.join(list02)
print(yingwen01)





