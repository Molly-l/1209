f=open('/home/tarena/.cache/.fr-WKOoNt/IO网络编程/dict.txt','r')
dict01={}

for line in f:
    list01=line.split(' ')
    # print(list01)
    dict01[list01[0]]=list01[1:-1]
f.close()
while True:
    w01=input('请输入查找的单词：')
    if w01 in dict01:
        print(' '.join(dict01[w01]))


