from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .models import Product,Category
# Create your views here.


def search(request):
    query = request.GET.get('query','')

    products = Product.objects.filter(Q(title__icontains = query)
                                      |Q(description__icontains=query))

    context={'query':query,'products':products}
    return render(request,'store/search.html',context)

def category_detail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    products = category.products.all()
    
    context={'category':category,
             'products':products,
             }
    
    return render(request,'store/category_detail.html',context)

def product_detail(request,category_slug,slug):
    product = get_object_or_404(Product,slug=slug)
    print('product.user.id',product.user.id)
    print('product.description',product.description)
    print('product.category.id',product.category.id)
    context={'product':product}
    return render(request,'store/product_detail.html',context)


