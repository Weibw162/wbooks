import sys
import os
import random

import django

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

django.setup()

from goods.models import Goods, GoodsCategory


class Updatetabandgoods:
    def updattabadndgoods(self):
        category_tab_id = [1, 27, 75, 99, 204, 284]
        GoodsCategory.objects.filter(pk__in=category_tab_id).update(is_tab=True)
        is_new_id = [random.randint(1, 89), random.randint(1, 89)]
        Goods.objects.filter(pk__in=is_new_id).update(is_new=True)
        is_hot_id = [random.randint(1, 89), random.randint(1, 89), random.randint(1, 89)]
        Goods.objects.filter(pk__in=is_hot_id).update(is_hot=True)


if __name__ == "__main__":
    add = Updatetabandgoods()
    add.updattabadndgoods()
