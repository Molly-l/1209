def score():
    while True:
        try:
            i=int(input('输入成绩：'))
            return i
        except:
            print('输入有误')
if __name__=='__main__':
    print(score())



