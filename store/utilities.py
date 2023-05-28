from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .cart import Cart

from .models import Order,OrderItem

def checkout(request,first_name,last_name,email,address,zipcode,city,amount):
    order = Order.objects.create(first_name=first_name,last_name=last_name,email=email
                                 ,address=address,zipcode=zipcode,city=city,paid_amount = amount)
    
    for item in Cart(request):
        OrderItem.objects.create(order=order,product=item['product'],price=item['product'].price,quantity=item['quantity'])
        
    #order.vendors.add(item['product'].vendor)
        return order

def notify_vendor(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    #for vendor in order.vendors.all():
    to_email = order.created_by.email
    print('vendor to_email',to_email)
    subject = 'new order'
    text_content = 'you have a new order!'
    html_content = render_to_string('store/email_notify_vendor.html',{'order':order})

    msg = EmailMultiAlternatives(subject,text_content,from_email,[to_email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    #for vendor in order.vendors.all():
    to_email = order.email
    print('customer to_email',to_email)
    subject = 'Order confirmation'
    text_content = 'Thanks for your order!'
    html_content = render_to_string('store/email_notify_customer.html',{'order':order})

    msg = EmailMultiAlternatives(subject,text_content,from_email,[to_email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
        
        
    
