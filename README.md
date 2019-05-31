# wbooks
基于Django框架，使用Django REST framework前后端分离技术搭建的网上图书商店

本项目基于某课网生鲜超市改编，进一步完善某些功能。(如有条件尽量支持[正版](https://coding.imooc.com/class/131.html))

项目配套前端地址：[Wbooks_Vue](https://github.com/Weibw162/Wbooks_Vue)

项目演示地址：[http://wbooks.weisapp.top](http://wbooks.weisapp.top)

项目API演示地址：[API](http://api.weisapp.top)

后台管理采用django-simpleui,一个Vue+Element-ui的现代主题：[后台开源地址](https://github.com/newpanjing/simpleui)

## 数据
+ [图书类别数据](https://github.com/Weibw162/wbooks/blob/master/db_tools/data/book_categories.py)
+ [图书数据](https://github.com/Weibw162/wbooks/blob/master/db_tools/data/book_data.py)
+ [热搜词条](https://github.com/Weibw162/wbooks/blob/master/db_tools/data/hotsearch_data.py)
+ [首页广告数据](https://github.com/Weibw162/wbooks/blob/master/db_tools/data/indexAd_data.py)
+ [轮播广告](https://github.com/Weibw162/wbooks/blob/master/db_tools/data/product_data.py)
+ [短信验证码数据](https://github.com/Weibw162/wbooks/blob/master/db_tools/data/verifycodes_data.py)
+ [收货地址数据](https://github.com/Weibw162/wbooks/blob/master/db_tools/data/address_data.py)

## 导入数据
+ [导入图书类别](https://github.com/Weibw162/wbooks/blob/master/db_tools/import_book_categories.py)
+ [导入图书数据](https://github.com/Weibw162/wbooks/tree/master/db_tools/import_book_data.py)
+ [设置导航、随机设定新品及热销](https://github.com/Weibw162/wbooks/tree/master/db_tools/add_tab_new_hot.py)
+ [导入热搜词条](https://github.com/Weibw162/wbooks/tree/master/db_tools/import_hotsearch.py)
+ [设置首页广告](https://github.com/Weibw162/wbooks/tree/master/db_tools/import_indexad.py)
+ [导入轮播图](https://github.com/Weibw162/wbooks/tree/master/db_tools/import_product.py)
+ [导入短信验证码数据](https://github.com/Weibw162/wbooks/tree/master/db_tools/import_verifycodes.py)
+ [生成用户](https://github.com/Weibw162/wbooks/tree/master/db_tools/import_user.py)
+ [随机添加用户收藏](https://github.com/Weibw162/wbooks/tree/master/db_tools/import_colection.py)
+ [图书进货](https://github.com/Weibw162/wbooks/tree/master/db_tools/stock_goods.py)
+ [更新用户信息并增加用户收货地址](https://github.com/Weibw162/wbooks/tree/master/db_tools/import_address_update_userinfo.py)
+ [随机加入购物车并生成订单](https://github.com/Weibw162/wbooks/tree/master/db_tools/create_order_test.py)
+ [随机对订单发货](https://github.com/Weibw162/wbooks/tree/master/db_tools/random_delivery.py)
+ [聚合脚本（一次性完成以上所有数据的导入）](https://github.com/Weibw162/wbooks/tree/master/db_tools/test.py)
