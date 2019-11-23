# import random
# random_number=random.randint(1,100)
# print(random.randint(1,100))
while True:

count=0
while count<3:  #0 1 2
    count +=1
    input_number=int(input('输入一个数字'))
    if input_number == random_number:
        print('猜对了',+str(count)+'次')
        break
    elif input_number > random_number:
        print('猜大了')
    else:
        print('猜小了')
else:
    print('你输了，正确的数字是'+)