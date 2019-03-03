from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from culture import models
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ()
    list_display = ['use_name', 'phone','add']

admin.site.unregister(User)
admin.site.register(models.user)
#admin.site.register(User)
admin.site.register(models.per,ArticleAdmin)
admin.site.register(models.com,ArticleAdmin)
admin.site.site_title = '文化创意产业公共服务后台'
admin.site.site_header = '文化创意产业公共服务后台'

# Register your models here.
