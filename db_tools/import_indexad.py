import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from goods.models import Goods, GoodsCategory, IndexAd
from db_tools.data.indexAd_data import indexad_data


class AddindexAd:
    def addindexad(self):
        indexad_list = []
        for indexad in indexad_data:
            indexAd = IndexAd()
            indexAd.goods = Goods.objects.filter(pk=indexad["book_id"])[0]
            indexAd.category = GoodsCategory.objects.filter(pk=indexad["cate_id"])[0]
            indexad_list.append(indexAd)

        IndexAd.objects.bulk_create(indexad_list)


if __name__ == "__main__":
    add = AddindexAd()
    add.addindexad()
