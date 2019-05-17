import requests
import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()


class RegistUser:
    def regist(self):
        for i in range(10):
            data = {
                "username": "1584200451%d" % (i),
                "code": "123%d" % (i),
                "mobile": "1584200451%d" % (i),
                "password": "123456"
            }
            requests.post("http://127.0.0.1:8000/api/users/", data=data)


if __name__ == "__main__":
    register = RegistUser()
    register.regist()
