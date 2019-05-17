import sys
import os
import random

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from goods.models import GoodsStock, Goods


class StockGoods:
    def stock(self):
        for count in range(3):
            for i in range(1, 90):
                goods = Goods.objects.filter(pk=i)[0]
                bid = float(goods.bid) * 0.95
                goods_stock = GoodsStock()
                goods_stock.goods = goods
                goods_stock.bid = bid
                goods_stock.stock_num = 50 * (random.randint(1, 7))
                goods_stock.save()


if __name__ == "__main__":
    stock = StockGoods()
    stock.stock()
