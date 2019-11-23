shangpin_info={
101:{'name':'倚天剑','price':10000},
102:{'name':'屠龙刀','price':10000},
103:{'name':'九阳神功','price':10000},
104:{'name':'九阴白骨爪','price':9999},
105:{'name':'乾坤大挪移','price':8888},
106:{'name':'七伤拳','price':7777}
}
# shangpin_info[101]['name']
gouwuche={
          }
caidan='''************
商店
************
按1购买
按2结算
************'''
def shangpin(a):
    for k,v in a.items():
        print(k,v['name'],v['price'])
def add_gouwuche(dict,che):
    while True:
        count=int(input('bianhao'))
        if count not in dict:
            print('bucunz')
            '''添加购物车函数'''
        count01=int(input('次数'))
        print('添加购物车')
        list01=[count01,dict[count]['price']]
        che[count]=list01
        break
def xianshi_gouwuc(c):
    for k,v in c.items():
        print(k,v[0],v[1])
def paying(gouwuche):
    money=float(input('金额'))
    zjiage=0
    for k,v in gouwuche.items():
            zjiage+=v[0]*v[1]
    if money>=zjiage:
        print('找零',money-zjiage)
    else:
        print('不够')
def f(shangpin_info,gouwuche):
    while True:
        key=int(input(caidan)   )
        if key==1:
            shangpin(shangpin_info)
            add_gouwuche(shangpin_info,gouwuche)

        if key==2:
            xianshi_gouwuc(gouwuche)
            paying(gouwuche)

f(shangpin_info,gouwuche)
