# -*- coding: utf-8 -*-
# Author:leali
# Description: 
# Version:v1.0
# Date:5/21/2018-1:25 PM


class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # property(price) =@property
        # 实际价格 = 原价 * 折扣
        new_price = 0
        try:
            # hasattr 可以判断属性是否存在，返回bool
            new_price = self.original_price * self.discount
        except AttributeError as error:
            print("AttributeError:", error)
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


if __name__ == "__main__":
    obj = Goods()
    print(obj.price)  # 获取商品价格
    obj.price = 200  # 修改商品原价
    print(obj.price)
    del obj.price  # 删除商品原价
    print(obj.price)
