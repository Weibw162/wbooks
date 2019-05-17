import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from goods.models import Goods, Banner
from db_tools.data.product_data import product_data


class AddProduct:
    def addproduct(self):
        product_list = []
        for product in product_data:
            banner = Banner()
            goods = Goods.objects.filter(pk=product["id"])
            if goods:
                banner.goods = goods[0]
            banner.image = product["image"]
            banner.index = product["index"]
            product_list.append(banner)
        Banner.objects.bulk_create(product_list)


if __name__ == "__main__":
    add = AddProduct()
    add.addproduct()
