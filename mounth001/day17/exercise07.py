list01=['孙悟空','白雪公主','贾宝玉']
list02=[101,102,103]
def my_zip():
    for i in range(len(list02)):
        yield (list01[i],list02[i])

for i in my_zip():
    print(i)

