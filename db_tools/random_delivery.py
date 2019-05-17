import sys
import os
import random

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from trade.models import OrderInfo

class RandomDelivery:
    def randomdelivery(self):
        delivery_list = []
        for i in range(50):
            delivery_list.append(random.randint(1,100))
        delivery_list = set(delivery_list)

        OrderInfo.objects.filter(pk__in=delivery_list).update(is_delivery=True)



if __name__ == "__main__":
    delivery = RandomDelivery()
    delivery.randomdelivery()