from django.contrib import admin
from .models import (Product,ProductVariantPrice,
                     ProductVariant,ProductImage,Variant)

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductVariantPrice)
admin.site.register(ProductVariant)
admin.site.register(ProductImage)
admin.site.register(Variant)
