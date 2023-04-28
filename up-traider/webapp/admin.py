from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from webapp.models import MenuItem

admin.site.register(MenuItem, MPTTModelAdmin)