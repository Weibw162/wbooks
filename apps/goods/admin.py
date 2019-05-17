from django.contrib import admin

from .models import Goods, GoodsStock, GoodsCategory, GoodsImage, Banner, HotSearchWords, GoodsCategoryBrand, IndexAd


class GoodsAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "author", "click_num", "sold_num", "fav_num", "goods_num", "bid", "market_price",
                    "shop_price", "is_new", "is_hot", "add_time"]
    search_fields = ['name', 'author']
    list_editable = ["is_hot", 'is_new']
    list_filter = ["click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "category__name", "add_time", ]
    style_fields = {"goods_desc": "ueditor"}
    list_per_page = 50

    class GoodsImagesInline(admin.TabularInline):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]


class GoodsStockAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "goods", 'stock_num', 'bid', 'stock_time']
    list_filter = ["goods", "stock_time"]
    list_per_page = 50


class GoodsCategoryAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "name", "code", "category_type", "parent_category", "is_tab", "add_time", "desc"]
    list_filter = ["category_type", "is_tab"]
    search_fields = ['name', 'code']
    list_editable = ["is_tab"]
    list_per_page = 50


class GoodsBrandAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "name", "category", "image", "desc", "add_time"]
    search_fields = ["name"]
    list_filter = ["category"]
    list_per_page = 50

    def get_context(self):
        context = super(GoodsBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
        return context


class BannerGoodsAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "index", "goods", "image", "add_time"]


class HotSearchAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "keywords", "index", "add_time"]


class IndexAdAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "category", "goods"]


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsStock, GoodsStockAdmin)
admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(Banner, BannerGoodsAdmin)
admin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)
admin.site.register(HotSearchWords, HotSearchAdmin)
admin.site.register(IndexAd, IndexAdAdmin)
