list01=[
    [0,1,2,3,4],
    [1,28,45,6,7],
    [20,7,3,65,2]
]
for i in list01[1]:
    print(i)
for i in range(len(list01)):

    print(list01[i][0])

list02=[]
for c in range(len(list01[0])):
    list02.append([])
    for i in range(len(list01)):
        list02[c].append(list01[i][c])
print(list02)