import sys
import os
import random
import datetime

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from users.models import UserProfile
from user_operation.models import UserAddress

from db_tools.data.address_data import address_data


class AddAdress:
    def addadress(self):
        useraddress_list = []
        for address in address_data:
            user = UserProfile.objects.filter(username="1584200451" + address["user"])[0]
            user.name = address["address"][0]["signer_name"][:-1]
            user.birthday = datetime.datetime.now().strftime('%Y-%m-%d')
            user.gender = random.choice(["male", "female"])
            user.email = user.mobile + "@163.com"
            user.save()
            for address_item in address["address"]:
                useraddress = UserAddress()
                useraddress.user = user
                useraddress.province = address_item["province"]
                useraddress.city = address_item["city"]
                useraddress.district = address_item["district"]
                useraddress.address = address_item["address"]
                useraddress.signer_name = address_item["signer_name"]
                useraddress.signer_mobile = address_item["signer_mobile"]
                useraddress_list.append(useraddress)
        UserAddress.objects.bulk_create(useraddress_list)

if __name__ == "__main__":
    address = AddAdress()
    address.addadress()
