from django.contrib import admin
from .models import Product,Vehicle

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_Id','Minimum_Order_Quantity')
    list_display_links = ['Product_Id']
    search_fields = ('Product_Id',)
    list_per_page = 25

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('Vehicle_Name','Product_Id','Capacity')
    list_display_links = ['Vehicle_Name']
    search_fields = ('Vehicle_Name',)
    list_per_page = 25



admin.site.register(Product,ProductAdmin)
admin.site.register(Vehicle,VehicleAdmin)
