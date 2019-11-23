gou_wu_che = {}
shnag_pin_info = {
    101: {'name': '倚天剑', 'price': 10000},
    102: {'name': '屠龙刀', 'price': 10000},
    103: {'name': '九阳神功', 'price': 10000},
    104: {'name': '九阴白骨爪', 'price': 9999},
    105: {'name': '乾坤大挪移', 'price': 8888},
    106: {'name': '七伤拳', 'price': 7777}
}
def shopping():
    while True:
        print('*'*12,'\n','商店','\n','*'*12,'\n','按1购买\n按2结算','\n','*'*12,sep='')

        key=int(input(':'))

        if key==1:
            show(shnag_pin_info)
            buying(gou_wu_che, shnag_pin_info)
        elif key==2:
            print('*'*12,'\n','购物车','\n','*'*12,sep='')

            show_gou_wu_che()

            return paying()
def paying():
    money = float(input('请输入金额：'))
    sum = 0
    for key in gou_wu_che:
        sum += float(gou_wu_che[key][0]) * float(gou_wu_che[key][1])
    if money > sum:
        print('应找回%.1f' % (money - sum))
        return 0
    else:
        print('金额不足')
        return 0
def show_gou_wu_che():
    for key in gou_wu_che:
        print(key, end=' ')
        for i in gou_wu_che[key]:
            print(i, end=' ')
        print()
def buying(gou_wu_che, shnag_pin_info):
    count = int(input('请输入商品编号'))
    if count not in shnag_pin_info:
        print('商品不存在')
    else:
        if count in gou_wu_che:
            gou_wu_che[count][0] += 1
        else:
            list01 = []
            list01.append(1)
            list01.append(shnag_pin_info[count]['price'])
            gou_wu_che[count] = list01
        print('添加到购物车')
def show(shnag_pin_info):
    for k, v in shnag_pin_info.items():
        print(k, end=' ')
        for i in v.values():
            print(i, end=' ')
        print()
shopping()