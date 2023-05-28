
from django.conf import settings
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from django.db.models import Q

from userprofile.models import Userprofile
from store.forms import ProductForm

from store.models import Product,Category,Order,OrderItem

# Create your views here.

def vendor_detail(request,pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(~Q(status=Product.DECOMMISSION))
    
    context={'user':user,'products':products}
    return render(request,'userprofile/vendor_detail.html',context)

@login_required
def my_store_order_detail(request,pk):
    order = get_object_or_404(Order,pk=pk)

    context={'order':order,'title':'Order Detail',}
    return render(request,'userprofile/my_store_order_detail.html',context)


@login_required
def add_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            slug = slugify(title)
            
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slug
            product.save()
            
            messages.success(request,'Product was added.')
            return redirect('my_store')
    else:
        form = ProductForm()
    
    context={'title':'Add','form':form,}
    return render(request,'userprofile/product_form.html',context)

@login_required
def edit_product(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES,instance = product)

        if form.is_valid():
            form.save()
            messages.success(request,'Product was updated.')
            return redirect('my_store')
    else:
        form = ProductForm(instance = product)
    
    context={'title':'Edit','form':form,
             'product':product,}
    return render(request,'userprofile/product_form.html',context)

@login_required
def decommission_product(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DECOMMISSION
    product.save()
    messages.success(request,'Product was decommission.')
    return redirect('my_store')

@login_required
def my_store(request):
    #products = request.user.products.exclude(status=Product.DECOMMISSION)
    products = request.user.products.filter(~Q(status=Product.DECOMMISSION))
    order_items = OrderItem.objects.filter(product__user=request.user)
    
    context={'title':'My store','products':products,
             'order_items':order_items,}
    
    return render(request,'userprofile/my_store.html',context)

@login_required
def myaccount(request):
    
    context={}
    return render(request,'userprofile/myaccount.html',context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()

            login(request,user)

            userprofile = Userprofile.objects.create(user=user)
            return redirect('frontpage')

    else:
        form =UserCreationForm()
    context = {'form':form}
    
    return render(request,'userprofile/signup.html',context)



            
            
    
