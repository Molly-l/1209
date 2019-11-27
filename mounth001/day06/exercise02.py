year=int(input('输入年份'))
month=int(input('输入月份'))
if month<1 or month>12:
    print('输入错误')
elif month==2:
    if year%4==0 and year%100!=0 or year%400==0:
         print(29)
    else:
        print(28)

list01=[31,28,31,30,31,30,31,31,30,31,30,31]

