import json
import stripe
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .utilities import *

from .models import Product,Category,Order,OrderItem
# Create your views here.

def add_to_cart(request,product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')

def success(request):

    context={'title':'Payment Success'}
    return render(request,'store/success.html',context)

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

@login_required
def checkout(request):
    cart = Cart(request)

    if cart.get_total_cost() == 0:
        return redirect('cart_view')

    if request.method == 'POST':
        data = json.loads(request.body)
        form = OrderForm(request.POST)
        
        #if form.is_valid():
        total_price = 0
        items = []

        for item in cart:
            product = item['product']
            total_price += product.price * int(item['quantity'])

            items.append({
                'price_data':{
                    'currency':'usd',
                    'product_data':{
                        'name':product.title,
                    },
                    'unit_amount':product.price
                },
                'quantity':item['quantity']
            })

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            #success_url=f'{settings.WEBSITE_URL}cart/success/',
            #cancel_url=f'{settings.WEBSITE_URL}cart/'
 
            success_url='http://127.0.0.1:8000/cart/success/',
            cancel_url='http://127.0.0.1:8000/cart/'
        )

        payment_intent = session.payment_intent

        order = Order.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            address = data['address'],
            zipcode = data['zipcode'],
            city = data['city'],
            created_by = request.user,
            is_paid = True,
            payment_intent = payment_intent,
            paid_amount = total_price
        )


        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity
            item = OrderItem.objects.create(order=order,product=product,price=price,quantity=quantity)
            
        cart.clear()  
        notify_customer(order)
        notify_vendor(order)           
        
        return JsonResponse({'session':session,'order':payment_intent})
    else:
        form = OrderForm()

    context={'title':'Checkout','cart':cart,
             'form':form,'pub_key':settings.STRIPE_PUB_KEY,
             }
    return render(request,'store/checkout.html',context)

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


