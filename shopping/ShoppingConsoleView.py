from shopping.OrderModel import OrderModel
from shopping.ShoppingCartController import ShoppingCartController

#控制台界面
class ShoppingConsoleView:
    def __init__(self):
        self.__controller = ShoppingCartController()

    # 选择菜单
    def __select_menu(self):
        while True:
            option = input('1键购买,2键结算,q键退出')#选项
            if option == 'q':
                break
            if option == '1':
                self.__buying()
            elif option == '2':
                self.__settlement()

    #购买
    def __buying(self):
        #打印商品信息
        self.__print_commodity()
        #创建订单
        self.__create_order()

    # 打印商品信息
    def __print_commodity(self):
        for  item in self.__controller.list_commodity_info:
            print("编号：%d,名称:%s,单价:%d" % (item.id,item.name,item.price) )

    # 创建订单
    def __create_order(self):
        while True:
            cid = int(input('请输入商品编号:'))
            #如果商品存在就退出 不存在就重新输入
            commodity = self.__controller.get_commodity_by_id(cid)
            if commodity:
                break
            else:
                print('商品不存在 请重新输入')

        count = int(input('请输入商品数量:'))
        order = OrderModel(cid,count)#订单模型
        self.__controller.add_order(order)

    # 结算
    def __settlement(self):
        #打印订单
        self.__print_order()
        #计算总价格
        total_price = self.__controller.get_tolal_price()
        #支付
        self.__pay(total_price)

    #支付
    def __pay(self,total_price):
        #接收用户输入 结算
        while True:
            moeny = float(input('总价%d元,请输入：' % total_price))
            if moeny>=total_price:
                print('购买成功，找零%.2f' % (moeny-total_price))
                break
            else:
                print('金额不足 请重新输入')

    # 打印订单
    def __print_order(self):
        for item in self.__controller.list_order:
            print('商品:%s,单价:%d,数量:%d' % (item.commodity.name,item.commodity.price,item.count) )


    def main(self):
        #选择菜单
        self.__select_menu()
