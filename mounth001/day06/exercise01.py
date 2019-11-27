list01=[]
for i in range(1,11):
    list01.append(i**2)

list01=[i**2 for i in range(1,11)]
list02=[i for i in list01 if i%2]
list03=[i for i in list01 if i%2==0]

# for i in list01:
#     if i%2:
#         list02.append(i)
print(list03)

# if 5%2=1
# if 5 % 2
# if 4%2=0
print(bool(5%2==1))
print(bool(5%2))

list01.clear()