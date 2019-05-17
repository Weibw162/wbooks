from django.db import models
from datetime import datetime

from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
    """
    书籍分类
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField('类别名', default="", max_length=30, help_text="类别名")
    code = models.CharField("类别code", default="", max_length=30, help_text="类别code")
    desc = models.TextField("类别描述", default="", help_text="类别描述")
    category_type = models.IntegerField("类目级别", choices=CATEGORY_TYPE, help_text="类目级别")
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别",
                                        help_text="父目录", related_name="sub_cat")
    is_tab = models.BooleanField("是否导航", default=False, help_text="是否导航")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "书籍类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    某一大类下的宣传商标
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, related_name='brands', null=True, blank=True,
                                 verbose_name="书籍类目")
    name = models.CharField("品牌名", default="", max_length=30, help_text="品牌名")
    desc = models.TextField("品牌描述", default="", max_length=200, help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "宣传品牌"
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand"

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    书籍
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="书籍类目")
    goods_sn = models.CharField(verbose_name="书籍唯一货号", max_length=50, default="")
    name = models.CharField(verbose_name="书名", max_length=100, )
    author = models.CharField(verbose_name="作者", max_length=100, default="")
    click_num = models.IntegerField(verbose_name="点击数", default=0)
    sold_num = models.IntegerField(verbose_name="书籍销售量", default=0)
    fav_num = models.IntegerField(verbose_name="收藏数量", default=0)
    goods_num = models.IntegerField(verbose_name="库存数量", default=0)
    market_price = models.DecimalField(verbose_name="市场价格", default=0, max_digits=5, decimal_places=2)
    shop_price = models.DecimalField(verbose_name="本店价格", default=0, max_digits=5, decimal_places=2)
    bid = models.DecimalField(verbose_name="书籍进价", default=0, max_digits=5, decimal_places=2)
    goods_brief = models.TextField(verbose_name="书籍简短描述", max_length=500)
    goods_desc = UEditorField(verbose_name="书籍内容介绍", imagePath="ueditor/images/", width=1000, height=300,
                              filePath="ueditor/files/", default='')
    goods_front_image = models.ImageField(verbose_name="封面图", upload_to="goods/images/", null=True, blank=True)
    is_new = models.BooleanField(verbose_name="是否新品", default=False)
    is_hot = models.BooleanField(verbose_name="是否热销", default=False)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = '书籍信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsStock(models.Model):
    """
    进货
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="书名")
    stock_num = models.IntegerField(verbose_name="数量", default=0)
    bid = models.DecimalField(verbose_name="进价", default=0, max_digits=5, decimal_places=2)
    stock_time = models.DateTimeField(verbose_name="进货时间", default=datetime.now)

    def save(self, *args, **kwargs):
        goods = self.goods
        goods_num = goods.goods_num
        bid = goods.bid
        goods.goods_num += self.stock_num
        goods.bid = (float(goods_num * bid) + float(self.stock_num * self.bid)) / (goods.goods_num)
        goods.save()
        super(GoodsStock, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "进货信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", related_name="images")
    image = models.ImageField(verbose_name="图片", upload_to="", null=True, blank=True)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        ordering = ["pk"]
        verbose_name = '商品轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    首页轮播的书籍
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="书名")
    image = models.ImageField(verbose_name="轮播图片", upload_to='banner')
    index = models.IntegerField(verbose_name="轮播顺序", default=0)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        ordering = ["pk"]
        verbose_name = '首页轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class IndexAd(models.Model):
    """
    书籍广告
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, related_name='category', verbose_name="书籍类目")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='goods')

    class Meta:
        ordering = ["pk"]
        verbose_name = '首页广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    搜索栏下方热搜词
    """
    keywords = models.CharField(verbose_name="热搜词", default="", max_length=20)
    index = models.IntegerField(verbose_name="排序", default=0)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        ordering = ["pk"]
        verbose_name = '热搜排行'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords
