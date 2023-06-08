from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from django.db.models import Q

from .forms import CustomUserCreationForm,UpdateProfileForm
from userprofile.models import Userprofile
from store.forms import ProductForm

from store.models import Product,Category

# Create your views here.

def vendor_detail(request,pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(~Q(status=Product.DECOMMISSION))
    
    context={'user':user,'products':products}
    return render(request,'userprofile/vendor_detail.html',context)

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
    
    context={'title':'My store','products':products,}
    return render(request,'userprofile/my_store.html',context)

@login_required
def myaccount(request):
    userprofiles = request.user
    
    context={'userprofiles':userprofiles}
    return render(request,'userprofile/myaccount.html',context)

def loginPage(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('username',username)
        print('password',password)

        userAuth = authenticate(request,username=username,password=password)
        print('userAuth',userAuth)

        if userAuth is not None:
            login(request,userAuth)
            return redirect('frontpage')
        
    context={'page':page}
    return render(request,'userprofile/signup_login.html',context)

def signup(request):
    page = 'signup'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            
            user=form.save(commit = False)
            user.save()
            userAuth = authenticate(request,username=user.username,password=request.POST['password1'])

            if userAuth is not None:
                login(request,userAuth)
                userprofile = Userprofile.objects.create(user=user)
                return redirect('frontpage')
        else:
            print("form content:",form.errors)
            print("form not valid check")
    else:
        form = CustomUserCreationForm()
    context = {'form':form,'page':page}
    
    return render(request,'userprofile/signup_login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')


def update_profile(request,pk):
    user = User.objects.get(pk=pk)
    form = UpdateProfileForm(instance = user)

    print('user:',user)
    if request.method == "POST":
        print('request.method is POST')
        form = UpdateProfileForm(request.POST,instance = user)

        if form.is_valid():
            form.save()
            print('form was save')
            messages.success(request,'User Profile was updated.')
            return redirect('myaccount')
        else:
            print('Form errors:', form.errors)
    
    context={'title':'Edit','form':form}
    return render(request,'userprofile/update_profile.html',context)

def delete_profile(request,pk):
    user = User.objects.get(pk=pk)

    print('user:',user)
    if request.method == "POST":
        name = user.username
        user.delete()
        messages.success(request,name + "account has been deleted.")
    
    context={'title':'Edit','user':user}
    return render(request,'userprofile/udeletee_profile.html',context)


            
            
    
