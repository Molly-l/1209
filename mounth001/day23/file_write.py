f=open('text.py','w')
# f=open('text.txt','ab')

# f.write('hello,死鬼\n'.encode())
# f.write('哎呀，干啥\n'.encode())
# f.close()

l=['hello world\n','哈哈哈哈\n']
f.writelines(l)
f.close()
