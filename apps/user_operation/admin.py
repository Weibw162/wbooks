from django.contrib import admin

from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "user", "goods", "add_time"]
    search_fields = ["user__username"]
    list_filter = ["user", "goods"]
    list_per_page = 50


class UserLeavingMessageAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["user", "message_type", "subject", "message", "file", "add_time"]
    list_filter = ["message_type", "user"]
    search_fields = ["subject"]
    list_per_page = 50


class UserAddressAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "user", "province", "city", "district", "address", "signer_name", "signer_mobile", "add_time"]
    list_filter = ["user", "province", "city", "district"]
    search_fields = ["address", "signer_name"]
    list_per_page = 50


admin.site.register(UserFav, UserFavAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
