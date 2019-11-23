a =input('请输入第一个变量：')
b =input('请输入第二个变量：')

price = input('请输入商品单价：')
price = float(price)
count = int(input('请输入商品数量：'))
money = float(input('请输入金额：'))
result = money - price * count
print('找零：',result)


