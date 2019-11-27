L=[1,2,3,4,5,6]
str01=''
for  i  in range(len(L)-1):
    str01+=str(L[i])
    str01+='|'
str01+=str(L[len(L)-1])
print(str01)

