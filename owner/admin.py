from django.contrib import admin
from django.contrib.admin.sites import site
from owner.models import Owner

class MyAdmin(admin.ModelAdmin):
    list_display = ('emaill','passwordd')
    
admin.site.register(Owner, MyAdmin)
# Register your models here.
