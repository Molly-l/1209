def result(shu,fuhao,shuzi):
    # shu=int(input('输入一个数字'))
    # fuhao=input('再输入一个运算符')
    # shuzi=int(input('再输入一个数字'))
    if fuhao =='+':
        # print(shu+shuzi)
        return shu+shuzi
    else:
        if fuhao =='-':
            # print(shu-shuzi)
            return shu-shuzi
        else:
            if fuhao =='*':
                # print(shu*shuzi)
                return shu*shuzi
            else:
                if fuhao =='/':
                    # print(shu/shuzi)
                    return shu/shuzi
                else:
                    print('运算符有误')
                    return 12
print(result(10,'*',5))
