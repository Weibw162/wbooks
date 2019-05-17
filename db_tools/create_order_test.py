import sys
import os
import random
import base64
import json

import requests
import jwt
import django

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

django.setup()

from MxShop.settings import SECRET_KEY
from user_operation.models import UserAddress
from goods.models import Goods
from users.models import UserProfile


class CreateOrder:
    def __init__(self):
        self.headers = {}  # 请求头
        self.total = 0  # 订单总价

    def login(self, name_end):
        user_login_data = {
            "username": "1584200451" + str(name_end),
            "password": 123456
        }
        response = requests.post("http://127.0.0.1:8000/api/login/", data=user_login_data)
        token_mes2 = json.loads(response.text)["token"].split(".")[1]
        missing_padding = 4 - len(token_mes2) % 4
        if missing_padding:
            token_mes2 += "=" * missing_padding
        encoded = jwt.encode(json.loads(base64.b64decode(token_mes2)), key=SECRET_KEY, algorithm='HS256').decode()
        self.headers = {
            "Authorization": "JWT {}".format(encoded)
        }
        return user_login_data

    def addshopcarts(self):
        for i in range(random.randint(1, 5)):
            goods_data = {
                "goods": random.randint(1, 89),
                "nums": random.randint(1, 5)
            }
            requests.post("http://127.0.0.1:8000/api/shopcarts/", data=goods_data, headers=self.headers)
            self.total += Goods.objects.filter(pk=goods_data["goods"])[0].shop_price * goods_data["nums"]

    def createorder(self):

        for i in range(10):
            user_login_data = self.login(i)
            self.addshopcarts()
            useraddress = random.choice(UserAddress.objects.filter(
                user=UserProfile.objects.filter(username=user_login_data["username"])[0]))
            order_data = {
                "address": useraddress.province + useraddress.city + useraddress.district + useraddress.address,
                "order_mount": self.total,
                "post_script": "用户未留言",
                "signer_name": useraddress.signer_name,
                "singer_mobile": useraddress.signer_mobile
            }
            requests.post("http://127.0.0.1:8000/api/orders/", data=order_data, headers=self.headers)
            self.total = 0


if __name__ == "__main__":
    createorder = CreateOrder()
    createorder.createorder()
