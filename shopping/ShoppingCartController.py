from shopping.CommodityModel import CommodityModel

#逻辑控制类
class ShoppingCartController:
    __init_order_id = 0
    def __init__(self):
        self.__list_order = []
        self.__list_commodity_info = self.__load_commodity()

    @property#只读，变私有
    def list_order(self):
        return self.__list_order
    # @list_order.setter #只写
    # def lis_order(self,v):
    #     if v>80:
    #         self.__list_order.append(v)

    @property
    def list_commodity_info(self):
        return self.__list_commodity_info

    #加载商品信息
    def __load_commodity(self):

        #商品列表
        return [
            CommodityModel(101,'倚天剑',10000),
            CommodityModel(102,'屠龙刀',10000),
            CommodityModel(103,'九阳神功',10000),
            CommodityModel(104,'九阴白骨爪',9999),
            CommodityModel(105,'乾坤大挪移',8888),
            CommodityModel(106,'七伤拳',7777),
        ]

    #添加订单
    def add_order(self,order_info):

        #获取订单信息，生成id
        order_info.id = self.__generate_order_id()
        self.__list_order.append(order_info)

    #生成订单id
    def __generate_order_id(self):
        ShoppingCartController.__init_order_id += 1
        return ShoppingCartController.__init_order_id

    # 计算总价格
    def get_tolal_price(self):
        total_price = 0
        for item in self.__list_order:
            total_price += item.count * item.commodity.price
        return total_price

    #获取指定的商品
    def get_commodity_by_id(self,id):
        for item in self.list_commodity_info:
            if item.id == id:
                return item
