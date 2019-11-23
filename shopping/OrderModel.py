class OrderModel:#订单模型
    def __init__(self,commodity,count,id = 0):
        self.id = id
        self.commodity = commodity
        self.count = count
