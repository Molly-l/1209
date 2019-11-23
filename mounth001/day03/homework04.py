i=int(input('输入利润'))
money=0
if i>100:
    money+=(i-100)*0.01
    i=100
if i>60:
    money+=(i-60)*0.015
    i = 60
if i>40:
    money+=(i-40)*0.03
    i = 40
if i>20:
    money+=(i-20)*0.05
    i =20
if i > 10:
    money += (i-10)*0.075
    i = 10
money += i * 0.1
print(money)

