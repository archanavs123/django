from django.contrib import admin
from.models import *
# Register your models here.
class District_display(admin.ModelAdmin):
    list_display=['name']
admin.site.register(District,District_display)












































































































































































































