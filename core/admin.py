from django.contrib import admin

# Register your models here.
from .models_1 import CustCategories, CustTypes, Customer

class CustTypesAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['name']

class CustCategoriesAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['name']

class CustomerAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['cust_name', 'city']


    admin.site.register(CustCategories, CustCategoriesAdmin)
admin.site.register(CustTypes, CustTypesAdmin)
admin.site.register(Customer, CustomerAdmin)