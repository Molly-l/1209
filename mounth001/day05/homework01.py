# list_01=[]
# while True:
#     zifuc=input('录入字符串')
#     if zifuc=='':
#         break
#     list_01.append(zifuc)
# print(list_01)




fibs=[0,1]
for i in range(15):
    a=fibs[i] + fibs[i + 1]
    fibs.append(a)
print(fibs)

