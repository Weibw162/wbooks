from django.contrib import admin

from .models import UserProfile, VerifyCode


class UserProfileAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "username", "birthday", "gender", "mobile", "email", "add_time"]
    search_fields = ["name", "mobile"]
    list_per_page = 50


class VerifyCodeAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ["pk", "code", "mobile", "add_time"]
    search_fields = ["mobile"]
    list_per_page = 50


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(VerifyCode, VerifyCodeAdmin)
