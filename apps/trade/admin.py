from django.contrib import admin

from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "user", "goods", "nums", "add_time"]
    search_fields = ["user__username"]
    list_filter = ["user", "goods"]
    list_per_page = 50


class OrderInfoAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "user", "order_sn", "pay_status", "pay_type", "post_script",
                    "order_mount", "signer_name", "singer_mobile", "address", "is_delivery", "pay_time", "add_time"]
    search_fields = ["user__username", ]
    list_filter = ["pay_status", "pay_type", "is_delivery", "pay_time", "add_time"]
    list_per_page = 50

    class OrderGoodsInline(admin.TabularInline):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]


admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(OrderInfo, OrderInfoAdmin)
