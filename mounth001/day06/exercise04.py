shangpin={}
while True:
    name=input('输入名称')
    price=input('输入单价')
    if name=='':
        break
    shangpin[name]=price
for name,price in shangpin.items():
    print('%s的单价%f'%(name,price))
if '游戏机' in shangpin:
    print('游戏机的价格是%f'%
          shangpin['游戏机'])
