from db_tools.import_book_categories import AddCate
from db_tools.import_book_data import AddGoods
from db_tools.add_tab_new_hot import Updatetabandgoods
from db_tools.import_hotsearch import Addhotsw
from db_tools.import_indexad import AddindexAd
from db_tools.import_product import AddProduct
from db_tools.import_verifycodes import AddVer
from db_tools.import_colection import Adduserfav
from db_tools.import_user import RegistUser
from db_tools.stock_goods import StockGoods
from db_tools.create_order_test import CreateOrder
from db_tools.import_address_update_userinfo import AddAdress
from db_tools.random_delivery import RandomDelivery

if __name__ == "__main__":

    #添加类目信息
    cate = AddCate()
    #添加商品信息
    goods = AddGoods()
    #更新tab、new、hot信息
    tab = Updatetabandgoods()
    #添加热搜词
    hotsw = Addhotsw()
    #添加首页类目推荐书籍广告
    indexad = AddindexAd()
    #添加轮播广告
    pro = AddProduct()
    #进货
    stock = StockGoods()


    #添加短信验证码
    ver = AddVer()
    #注册用户
    register = RegistUser()
    #添加用户收藏
    userfav = Adduserfav()
    #添加用户收货地址
    address = AddAdress()
    #用户下单
    order = CreateOrder()
    #随机发货
    delivery = RandomDelivery()
    
    cate.addcate()
    goods.addgoods()
    tab.updattabadndgoods()
    hotsw.addhotsw()
    indexad.addindexad()
    pro.addproduct()
    stock.stock()

    ver.addver()
    register.regist()
    userfav.adduserfav()
    address.addadress()
    for i in range(10):
        order.createorder()
    delivery.randomdelivery()
