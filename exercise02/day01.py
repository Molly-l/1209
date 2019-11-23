list01=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
# list02=[
#     [1,5,9,13]
# ]
list02=[]
for i in range(len(list01)):
    list02.append([])
    for c in range(len(list01[i])):
        list02[i].append(list01[c][i])
print(list02)



