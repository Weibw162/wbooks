from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

User = get_user_model()


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="书籍")
    nums = models.IntegerField("购买数量", default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)


class OrderInfo(models.Model):
    """
    订单信息
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("paying", "待支付"),
    )
    PAY_TYPE = (
        ("alipay", "支付宝"),
        ("wechat", "微信"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    order_sn = models.CharField(verbose_name="订单编号", max_length=30, null=True, blank=True, unique=True)
    pay_status = models.CharField(verbose_name="订单状态", choices=ORDER_STATUS, default="paying", max_length=30)
    pay_type = models.CharField(verbose_name="支付类型", choices=PAY_TYPE, default="alipay", max_length=10)
    post_script = models.CharField(verbose_name="订单留言", default="用户未添加留言", max_length=200)
    order_mount = models.DecimalField(verbose_name="订单金额", default=0.0, max_digits=6, decimal_places=2)
    pay_time = models.DateTimeField(verbose_name="支付时间", null=True, blank=True)
    is_delivery = models.BooleanField(verbose_name="是否发货",default=False)
    address = models.CharField(verbose_name="收货地址", max_length=100, default="")
    signer_name = models.CharField(verbose_name="签收人", max_length=20, default="")
    singer_mobile = models.CharField(verbose_name="联系电话", max_length=11)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    订单内的商品详情
    """
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单信息", related_name="goods")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="书籍")
    goods_num = models.IntegerField(verbose_name="书籍数量", default=0)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
