from django.shortcuts import render,get_object_or_404

from .models import Product
# Create your views here.

def product_detail(request,slug):
    product = get_object_or_404(Product,slug=slug)
    context={'product':product}
    return render(request,'store/product_detail.html',context)


