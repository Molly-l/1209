word = input("单词:")

# 打开文件
# f = open('dict.txt')
with open('4.txt') as f: # 以只读方式生成f对象
    data = f.read()
    print(data)


for line in f:
    w = line.split(' ')[0]
    # 遍历的单词已经大于目标,说明找不到了
    if w > word:
        print("没有找到该单词")
        break
    elif w == word:
        print(line)
        break
else:
    print("没有找到该单词")

f.close()