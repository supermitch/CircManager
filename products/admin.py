from products.models import Product
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)	
