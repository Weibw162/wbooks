import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from goods.models import Goods, GoodsCategory, GoodsImage
from db_tools.data.book_data import book_data


class AddGoods:
    def addgoods(self):
        for books_cate in book_data:
            category = GoodsCategory.objects.filter(pk=books_cate["category"])
            if category:
                for book in books_cate["books"]:
                    goods = Goods()
                    goods.category = category[0]
                    goods.name = book["name"]
                    goods.goods_sn = book["ISBN"]
                    goods.author = book["author"]
                    goods.click_num = goods.sold_num = goods.fav_num = 0
                    goods.goods_num = 200
                    goods.shop_price = book["shop_price"]
                    goods.market_price = goods.shop_price * 1.25
                    goods.bid = goods.shop_price * 0.8
                    goods.goods_brief = book["goods_brief"]
                    goods.goods_desc = book["goods_desc"]
                    goods.goods_front_image = book["images"][0]
                    goods.is_hot = goods.is_new = False
                    goods.save()

                    book_image_list = []
                    for book_image in book["images"]:
                        book_image_instance = GoodsImage()
                        book_image_instance.image = book_image
                        book_image_instance.goods = goods
                        book_image_list.append(book_image_instance)
                    GoodsImage.objects.bulk_create(book_image_list)


if __name__ == "__main__":
    add = AddGoods()
    add.addgoods()
