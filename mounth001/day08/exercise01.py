#
# def shu(list01):
#
#     list02=[]
#     for c in range(len(list01[0])):
#         list02.append([])
#         for i in range(len(list01)):
#             list02[c].append(list01[i][c])
#
#             list02[c][i]=list01[i][c]
#     # print(list02)
#     return list02
#
# list01=[
#         [0,1,2,3,4],
#         [1,28,45,6,7],
#         [20,7,3,65,2]
#     ]
# print(shu(list01))

list02=[]
# list02[0]=line
line=[]
list01=[
        [0,1,2,3,4],
        [1,28,45,6,7],
        [20,7,3,65,2]
    ]
# list01[0][0]
# list01[1][0]
# list01[2][0]
# line.append(list01[0][0])
# line.append(list01[1][0])
# line.append(list01[2][0])

for c in range(len(list01[0])):
    list02.append([])
    for i in range(len(list01)):
        list02[c].append(list01[i][c])

print(list02)

