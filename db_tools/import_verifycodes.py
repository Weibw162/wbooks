import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from db_tools.data.verifycodes_data import verifycodes_data
from users.models import VerifyCode


class AddVer:
    def addver(self):
        verifycode_list = []
        for verifycode in verifycodes_data:
            verfy = VerifyCode()
            verfy.code = verifycode["code"]
            verfy.mobile = verifycode["mobile"]
            verifycode_list.append(verfy)
        VerifyCode.objects.bulk_create(verifycode_list)


if __name__ == "__main__":
    add = AddVer()
    add.addver()
