from django.contrib import admin

from shop.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'price', 'available',
                    'for_promo')
    list_filter = ('brand', 'category', 'price', 'available')
    list_editable = ('available', 'for_promo')


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
