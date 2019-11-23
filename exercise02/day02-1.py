# 3.题目：按|分隔L列表。
#     L=[1,2,3,4,5,6]
#   实现效果：   1|2|3|4|5|6
L=[1,2,3,4,5,6]
# L01=[]
# for i in range(len(L)):
   # L[i]=str(L[i])
   #  L01.append(str(L[i]))

# str01='|'.join(L01)
# print(str01)
print('|'.join(str(i) for i in L))