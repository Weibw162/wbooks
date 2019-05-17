import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from goods.models import GoodsCategory
from db_tools.data.book_categories import book_categories


class AddCate:
    def addcate(self):
        # 一级分类
        for lev1_cat in book_categories:
            lev1_intance = GoodsCategory()
            lev1_intance.code = lev1_cat["cate_code"]
            lev1_intance.name = lev1_cat["cate_name"]
            lev1_intance.category_type = 1
            lev1_intance.save()

            # 二级分类
            for lev2_cat in lev1_cat["sub_cate"]:
                lev2_intance = GoodsCategory()
                lev2_intance.code = lev2_cat["cate_code"]
                lev2_intance.name = lev2_cat["cate_name"]
                lev2_intance.category_type = 2
                lev2_intance.parent_category = lev1_intance
                lev2_intance.save()

                # 三级分类
                for lev3_cat in lev2_cat["sub_cate"]:
                    lev3_intance = GoodsCategory()
                    lev3_intance.code = lev3_cat["cate_code"]
                    lev3_intance.name = lev3_cat["cate_name"]
                    lev3_intance.category_type = 3
                    lev3_intance.parent_category = lev2_intance
                    lev3_intance.save()


if __name__ == "__main__":
    add = AddCate()
    add.addcate()
