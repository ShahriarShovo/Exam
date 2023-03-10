from .models import ProductVariant

def get_product_variant(request):
    product_variant=ProductVariant.objects.all()

    context={
        'product_variant':product_variant
    }
    return context