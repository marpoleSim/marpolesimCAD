from django.contrib import admin

# Register your models here.

from .models import UserType, CompanyInfo, UserInfo

admin.site.register(UserType)
admin.site.register(CompanyInfo)
admin.site.register(UserInfo)
