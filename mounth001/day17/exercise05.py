list01 = [5, 8, 4, 78, 6, 23, 45, 10]
# def even_num():
#     # list02=[]
#     for i in list01:
#         if i%2==0:
#             yield i
#
# iterator=even_num()
# for item in iterator:
#     print(item)

# 生成器方法：
# def greater10():
#     for i in list01:
#         if i>10:
#             yield i
#
# e01=greater10()
# for i in e01:
#     print(i)


# 传统方法：
def greater10():
    list02=[]
    for i in list01:
        if i>10:
            list02.append(i)
    return list02

e01=greater10()
for i in e01:
    print(i)