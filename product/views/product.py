from django.views import generic

from product.models import Variant
from product.models import Product
from django.shortcuts import render


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
    



class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'product'
    paginate_by = 3
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if queryset.exists():
            return queryset
        else:
            return []
        
    def get_context_data(self,*args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        context['product_count']=Product.objects.count()
        return context 
    




