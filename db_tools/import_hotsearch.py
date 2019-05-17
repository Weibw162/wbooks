import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django

django.setup()

from goods.models import HotSearchWords
from db_tools.data.hotsearch_data import hotkey


class Addhotsw:
    def addhotsw(self):
        hotsw_list = []
        for keyword in hotkey:
            hotsw = HotSearchWords()
            hotsw.index = keyword["index"]
            hotsw.keywords = keyword["keywords"]
            hotsw_list.append(hotsw)
        HotSearchWords.objects.bulk_create(hotsw_list)


if __name__ == "__main__":
    add = Addhotsw()
    add.addhotsw()
