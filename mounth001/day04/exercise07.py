
# chang=input('输入长')
# kuan=input('输入宽')
# zhouchang=(chang+kuan)*2
# mianji=chang*kuan
# print('矩形的长为%d,宽为%d,周长%d,面积%d'%
#       (chang,kuan,zhouchang,))
def zm(chang,kuan):
    # chang=input('输入长')
    # kuan=input('输入宽')
    zhouchang=(chang+kuan)*2
    mianji=chang*kuan
    return (zhouchang,mianji)
print(zm(12,10)[1])