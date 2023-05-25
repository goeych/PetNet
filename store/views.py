from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .cart import Cart

from .models import Product,Category
# Create your views here.

def add_to_cart(request,product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')

def change_quantity(request,product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(product_id,quantity,True)

    return redirect('cart_view')
    
            

def remove_from_cart(request,product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart_view')
    
def cart_view(request):
    cart = Cart(request)

    context={'title':'Cart','cart':cart}

    return render(request,'store/cart_view.html',context)


def search(request):
    query = request.GET.get('query','')

    products = Product.objects.filter(~Q(status=Product.DECOMMISSION)).filter(Q(title__icontains = query)
                                      |Q(description__icontains=query))

    context={'query':query,'products':products}
    return render(request,'store/search.html',context)

def category_detail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    products = category.products.filter(~Q(status=Product.DECOMMISSION))
    
    context={'category':category,
             'products':products,
             }
    
    return render(request,'store/category_detail.html',context)

def product_detail(request,category_slug,slug):
    ##product = get_object_or_404(Product,slug=slug)

    #product = get_object_or_404(Product.objects.filter(slug=slug, ~Q(status=Product.DECOMMISSION)))

    #product = get_object_or_404(Product, slug=slug, ~Q(status=Product.DECOMMISSION))
    cart = Cart(request)
    print('cart.get_total_cost:',cart.get_total_cost())
    product = get_object_or_404(Product.objects.exclude(status=Product.DECOMMISSION).filter(slug=slug))
    
    print('product.user.id',product.user.id)
    print('product.description',product.description)
    print('product.category.id',product.category.id)
    context={'product':product}
    return render(request,'store/product_detail.html',context)


