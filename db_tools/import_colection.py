import sys
import os
import random

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from goods.models import Goods
from users.models import UserProfile
from user_operation.models import UserFav


class Adduserfav:
    def adduserfav(self):
        users = UserProfile.objects.filter(username__contains="158")

        fav_list = []
        for user in users:
            goods_list = []
            for i in range(25):
                id = random.randint(1, 89)
                if id not in goods_list:
                    goods = Goods.objects.filter(pk=id)[0]
                    goods_list.append(id)
                    userfav = UserFav()
                    userfav.goods = goods
                    userfav.user = user
                    fav_list.append(userfav)
        UserFav.objects.bulk_create(fav_list)


if __name__ == "__main__":
    add = Adduserfav()
    add.adduserfav()
