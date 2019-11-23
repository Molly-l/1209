# list01=[4,2,5,1,8,7,15,6]
# for n in range(len(list01)):
#     for i in range(len(list01)-1-n):
#         if list01[i]>list01[i+1]:
#             list01[i],list01[i+1]=list01[i+1],list01[i]
#
# print(list01)

list01=[4,2,5,1,8,7,15,6]
# [1, 4, 5, 2, 8, 7, 15, 6]
for c in range(len(list01)-1):
    for i in range(c+1,len(list01)):
        if list01[c]>list01[i]:
            list01[c],list01[i]=list01[i],list01[c]

# for i in range(2,len(list01)):
#     if list01[1]>list01[i]:
#         list01[1],list01[i]=list01[i],list01[1]

print(list01)


# list03=[4,2,5,1,8,7,15,6,4,2,5,1,8,7,15,6]
#
# for i in range(len(list03)):
#     print(list03[i],end=' ')
#     if (i+1)%3==0:
#         print()
a=55
print('a41'+' '+'b',1,end='\n')
print('a41','b',1,sep='*')

print(6,'=',end='',sep='')
print(1,2,3,sep='+')
# 6=1+2+3

print('a','b',1)


