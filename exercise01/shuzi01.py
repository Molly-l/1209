# a=int(input('输入第一个数字'))
# b=int(input('输入第二个数字'))
# if a<b:
#     print('输出b',b)
# elif a=b:
#     print('输出a',a)
# else:
#     print('输出a',a)


# a=int(input('输入第一个数字'))
# b=int(input('输入第二个数字'))
# c=int(input('输入第三个数字'))
# if a<b:
#     print('a<b',b)
#     if b<c:
#         print('输出c',c)
#     else:
#         print('输出b',b)
#
# else:
#     print('a>b',a)
#     if a<c:
#         print('输出c',c)
#     else:
#         print('输出a',a)
#


# a=int(input('输入第一个数字'))
# b=int(input('输入第二个数字'))
# c=int(input('输入第三个数字'))
# d=int(input('输入第四个数字'))
# if a>b:
#     print('a>b',a)
#     else:
#         print('输出b',b)
#         if b>c:
#             print('输出b',b)
#         else:
#             print('输出c',c)
#             if c>d:
#                 print('输出c', c)
#             else:
#                 print('输出d', d)
#
# else:
#     print('b>a',a)
a=int(input('输入第一个数字'))
b=int(input('输入第二个数字'))
c=int(input('输入第三个数字'))
d=int(input('输入第四个数字'))
max_value=a
if max_value<b:
    max_value=b
if max_value<c:
    max_value=c
if max_value<d:
    max_value=d
print('输出',max_value)