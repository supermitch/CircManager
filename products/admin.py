from products.models import Product, Promo
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)	

class PromoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Promo, PromoAdmin)
