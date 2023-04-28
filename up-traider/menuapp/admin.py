from django.contrib import admin
from menuapp.models import MenuItem
from mptt.admin import MPTTModelAdmin
# Register your models here.

class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(MenuItem, MenuItemMPTTModelAdmin)