#with 语句里，不用close,自动关闭文件
with open('w01.txt','r+') as f:
    e=f.read()
    # e=f.readline()
    # e=f.readline()

    # f.write()
    # f.writelines()

    print(e)