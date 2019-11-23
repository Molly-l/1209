def order(list):
    for i in range(len(list)-1):
        for c in range(i+1,len(list)):
            if list[i]>list[c]:
                list[i],list[c]=list[c],list[i]

list01=[5,7,8,1,6,9]
order(list01)
print(list01)