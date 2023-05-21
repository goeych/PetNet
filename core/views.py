from django.shortcuts import render

from store.models import Product

# Create your views here.

def frontpage(request):
    products = Product.objects.all()[0:6]

    context={'products':products}
    return render(request,'core/frontpage.html',context)

def about(request):

    context={}
    return render(request,'core/about.html',context)

