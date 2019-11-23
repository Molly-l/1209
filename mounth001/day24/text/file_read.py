try:
    f=open("w01.txt",'r')
except Exception as e:
    print(e)
e=f.read()
    # hello world
    # guihjk
    # jkl

# e=f.readline()
    # hello world

# e=f.readlines()
    # ['hello world\n', 'guihjk\n', 'jkl']
print(e)

# for l in f:#变量名l:表示文件中的一行，对象本身也是一个可迭代对象
#     print(l)

#     hello world
#
#     guihjk
#
#     jk
# for i in e:
#     print(i)
# e=open('w01.txt','w')
f.close()