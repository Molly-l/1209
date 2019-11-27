# dict01={i:i**2 for i in range(10) if i>5}
# print(dict01)


dict01={}
list01=['张三丰','翠山','无忌']
list02=['无忌','赵敏','芷若']
list03=[101,102,103]
dict01={i:len(i) for i in list01}
print(dict01)

dict02={list02[i]:list03[i] for i in range(len(list02))}
print(dict02)


dict01={}
i=['北京']
list01=['烤鸭','豆汁','炸酱面','驴打滚']
list02=['故宫','天安门','天坛']

dict01={i:list01 for i in list01}
print(dict01)
