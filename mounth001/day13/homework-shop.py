class ShangPinModel:
    def __init__(self,id,name,price):
        self.name=name
        self.price=price
        self.id=id

class DingdanModel:
    def __init__(self,count,id,price=0):
        self.count=count
        self.id = id
        self.price=price

class ShangPinManagerController:
    def __init__(self):
        self.__shangpin_list=[
            ShangPinModel(101,'倚天剑',10000),
            ShangPinModel(102, '屠龙刀', 10000),
            ShangPinModel(103,'九阳神功',10000)
        ]
        self.__cart_list = []

    @property
    def shangpin_list(self):
        return self.__shangpin_list

    @property
    def cart_list(self):
        return self.__cart_list

    def print_info(self):
        print('*' * 50)
        for i in self.__shangpin_list:
            print(i.id,i.name,i.price)
        print('*' * 50)

    def add_cart(self,id,count):

        dingdan = DingdanModel(count,id)

        for i in self.__shangpin_list:
            if i.id==id:
                dingdan.price=i.price
                break

        self.__cart_list.append(dingdan)


    def calc_total_price(self):
        sum01=0
        for i in self.__cart_list:
            sum01 +=float(i.price)*int(i.count)
            print(i.price,i.count)

        return sum01


class ShangPinView:

    def __init__(self):
        self.gh_lis=ShangPinManagerController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __display_menu(self):
        print('''
************
商店
************
按1购买
按2结算
按q退出
************
        ''')

    def __select_menu_item(self):
        item = input(':')
        if item == 'q':
            pass
        if item == '1':
            self.__display_shangpin()
            self.__add_cart()

        elif item == '2':
            zong=self.__calc_total_price()
            self.__paying(zong)

    def __display_shangpin(self):
        self.gh_lis.print_info()
    def __add_cart(self):
        id=int(input('输入id'))
        count=int(input('输入数量'))
        self.gh_lis.add_cart(id,count)

    def __calc_total_price(self):
        return self.gh_lis.calc_total_price()
    def __paying(self,zong_jia):
        while True:
            money = float(input('总价为%d元，请输入金额：' % zong_jia))
            if money >= zong_jia:
                print('购买成功，找零%.2f' % (money - zong_jia))
                self.gh_lis.cart_list.clear()
                break
            else:
                print('金额不足，请重新输入')
# view=ShangPinView()
# view.main()
co=ShangPinManagerController()
co.shangpin_list[0].name

# a=ShangPinModel(101,'倚天剑',10000)
#
# list01=[]
#
# list01.append(a)
#
# list01=[ShangPinModel(101,'倚天剑',10000)]

# shang_pin_info = {
#     101: {'name': '倚天剑', 'price': 10000},
#     102: {'name': '屠龙刀', 'price': 10000},
#     103: {'name': '九阳神功', 'price': 10000},
#     104: {'name': '九阴白骨爪', 'price': 9999},
#     105: {'name': '乾坤大挪移', 'price': 8888},
#     106: {'name': '七伤拳', 'price': 7777},
# }
# # 定义购物车清单
# cart_info = []
# prompt = '''************
# 商店
# ************
# 按1购买
# 按2结算
# 按q退出
# ************
# '''
# #菜单
# #提示字符串 让用户按1  2  q
# #如果q
# #退出
# #如果1
# #购物功能
# #如果2
# #结算功能
# def selcet_menu():
#     while True:
#         item = input(prompt)
#         if item == 'q':
#             break
#         if item == '1':
#             buying()
#         elif item == '2':
#             settlment()
# #购物功能
# #显示商品
# #检测商品是否存在
# #添加到购物车清单
# def buying():
#     print_info()
#     create_order()
#     print('添加购物车成功')
# # 显示商品
# def print_info():
#     print('*' * 50)
#     for key, value in shang_pin_info.items():
#         print('%d     %s     %d' % (key, value['name'], value['price']))
#     print('*' * 50)
# #检测商品是否存在
# def check_id():
#     while True:
#         cid = int(input('请输入商品编号：'))
#         if cid in shang_pin_info:
#             break
#         else:
#             print('商品不存在，请重新输入！')
#     return cid
# # 添加到购物车清单
# def create_order():
#     #需要合法的商品编号 由check_id提供
#     cid = check_id()
#     count = int(input('请输入商品数量：'))
#     # 如果商品编号正确　加购物车
#     cart_info.append({'cid': cid, 'count': count})
# #结算功能
# #打印购物清单
# #计算总价格
# #接受用户输入的金额
# #支付
# def settlment():
#     print_order()
#     total_price = calc_total_price()
#     paying(total_price)
# #打印订单
# def print_order():
#     print('*' * 50)
#     print('购物车')
#     print('*' * 50)
#     for item in cart_info:
#         price = shang_pin_info[item['cid']]['price']
#         print('%d     %d      %d' % (item['cid'], item['count'], item['count'] * price))
#     print('*' * 50)
# #计算总价格
# def calc_total_price():
#     zong_jia = 0
#     for order in cart_info:
#         price = shang_pin_info[order['cid']]['price']
#         zong_jia += order['count'] * price
#
#     return zong_jia
# #接受用户输入 完成支付
# def paying(zong_jia):
#     while True:
#         money = float(input('总价为%d元，请输入金额：' % zong_jia))
#         if money >= zong_jia:
#             print('购买成功，找零%.2f' % (money - zong_jia))
#             cart_info.clear()
#             break
#         else:
#             print('金额不足，请重新输入')
#
# selcet_menu()

