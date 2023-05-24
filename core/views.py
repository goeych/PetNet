from django.shortcuts import render
from django.db.models import Q

from store.models import Product

# Create your views here.

def frontpage(request):
    #products = Product.objects.exclude(status=Product.DECOMMISSION)
    products = Product.objects.filter(~Q(status=Product.DECOMMISSION))

    context={'products':products}
    return render(request,'core/frontpage.html',context)

def about(request):

    context={}
    return render(request,'core/about.html',context)

