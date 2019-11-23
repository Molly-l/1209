sum_number=0
n=10
while n<51:
    unit=n%10
    if unit == 3 or unit == 6 or unit == 9:
        n +=1
        continue
    sum_number +=n
    n +=1

print(sum_number)










