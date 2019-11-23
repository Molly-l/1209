def run(year):
    # year = int(input('请输入年份:'))
    result = year % 4 == 0 and year % 100 !=0 or year % 400 == 0
    # print(result)
    return result
print(run(1998))