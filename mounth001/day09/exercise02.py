list01=[2,2,0,0]
# list02=[]
# for i in list01:
#     if i:
#         list02.append(i)
# for i in list01:
#     if i==0:
#         list02.append(i)
# print(list02)
#
# def zero_to_end(list_target):
#     new_list=[]
#     for i in list_target:
#         if i != 0:
#             new_list.append(i)
#     for i in range(list_target.count(0)):
#         new_list.append(0)
#         return new_list
#
# def  zero_to_end(list_target):
#     new_list=[i for i in list_target if i != 0]
#     new_list+=[0]*list_target.count(0)
#     return new_list
# print(zero_to_end([0,4,0,0]))

# def  zero_to_end(list_target):
#     for i in list_target:
#         if i == 0:
#             list_target.remove(i)
#             list_target.append(0)
#     return list_target
# print(zero_to_end(list01))
#
#
# def  zero_to_end(list_target):
#     for i in range(len(list_target)-1,-1,-1):
#         if list_target[i] == 0:
#             list_target.remove(list_target[i])
#             list_target.append(list_target[i])
#     return list_target
# print(zero_to_end(list01))

#
# def  zero_to_end(list_target):
#     for i in list_target[::-1]:
#         if not i:
#             list_target.remove(i)
#             list_target.append(i)
#     return list_target
# print(zero_to_end(list01))


def merge(list_target):

    for i in list_target:
        if i == 0:
            list_target.remove(i)
            list_target.append(0)
    for i in range(len(list_target)-1):
        if list_target[i]==list_target[i+1]:
            list_target[i] += list_target[i+1]
            del list_target[i+1]
            list_target.append(0)
    return list_target
print(merge(list01))
game_map=[
    [2,0,0,2],
    [4,4,2,2],
    [2, 4,0,4],
    [2, 0, 0, 2]

]

def game(list_target):
    for i in list_target:
        merge(i)
    return list_target
print(game(game_map))






