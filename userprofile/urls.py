from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='userprofile/login.html'),name='login'),
    path('signup/',views.signup,name='signup'),
    path('my-store/',views.my_store,name='my_store'),
    path('my-store/order-detail/<int:pk>/',views.my_store_order_detail,name='my_store_order_detail'),
    path('my-store/add-product/',views.add_product,name='add_product'),
    path('my-store/edit-product/<int:pk>/',views.edit_product,name='edit_product'),
    path('my-store/decommission_product/<int:pk>/',views.decommission_product,name='decommission_product'),
    path('vendors/<int:pk>/',views.vendor_detail,name='vendor_detail'),
    path('myaccount/',views.myaccount,name='myaccount'),

    ]
