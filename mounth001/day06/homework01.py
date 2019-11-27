# dict01={}
# while True:
#     list01 = []
#     name = input('北京','四川')
#
#     m01=['烤鸭','豆汁','炸酱面','驴打滚']
#     list01.append(m01)
#     j01=['故宫','天安门','天坛']
#     list01.append(j01)
#     m02=['火锅', '串串', '毛血旺']
#     j02=['峨眉山', '九寨沟', '春熙路']
#     dict01[name] = list01
#     for item in name:
#         print('名字是%s','美食是%s','景区是%s' %
#               (item, dict01[item][0], dict01[item][1]))
#     # for key, value in dict01.items():
#     #     print('名字是%s','美食是%s','景区是%s' %
#     #           (key, value[0], value[1]))
#
#     # dict01[name]=list_m and list_j
# print(dict01)





dict01={
'北京':
    {'美食':['烤鸭','豆汁','炸酱面'],
    '景区':['故宫','天安门','天坛']},
'四川':
    {'美食': ['火锅', '串串', '毛血旺'],
    '景区': ['峨眉山', '九寨沟', '春熙路']}
}
dict05={'北京':1,'四川':2}
for key in dict05:
    print(key,dict05[key])

dict01={}

str01='this is a test string'
for i in str01:
    if i in dict01:
        dict01[i]+=1
    else:
        dict01[i]=1
print(dict01)


# dict01.setdefault(i,0)
# dict01[i] +=1