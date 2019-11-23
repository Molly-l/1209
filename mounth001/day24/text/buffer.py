# f=open('w01.txt','w',1)
# #1:行缓冲buffering(写完的行缓冲)
f=open('w01.txt','w')
# f.write('111')
# ['111\n','fujhk ','','dfyt']
f.write('111\n')
f.write('77777\n')
# f.flush()#手动刷新缓冲之前所有操作
i=input('**')
f.write('fujhk ')
f.close()