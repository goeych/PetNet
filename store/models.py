from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image

from django.core.files import File


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
class Product(models.Model):

    ACTIVE = 'active'
    INACTIVE = 'inactive'
    CAL_PROGRESS = 'cal_progress'
    DECOMMISSION= 'decommission'

    STATUS = (
        (ACTIVE,'Active'),
        (INACTIVE,'Inactive'),
        (CAL_PROGRESS,'Cal_progress'),
        (DECOMMISSION,'Decommission'),
        )
    
    user = models.ForeignKey(User,related_name = 'products',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name = 'products',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/product_images/',blank=True,null=True)
    thumbnail = models.ImageField(upload_to='uploads/product_image/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)
    status = models.CharField(max_length=50,choices=STATUS,default=ACTIVE,blank =True,null=True)

    class Meta:
        ordering =['-created_at',]

    def __str__(self):
        return self.title
    
    def get_display_price(self):
        return self.price / 100

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
        
    def make_thumbnail(self,image,size=(300,200)):
        img = Image.open(image)
        img= img.convert('RGB')# Convert to RGB color mode
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG',quality=85)

        thumbnail = File(thumb_io,name=image.name)

        return thumbnail


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    paid_amount = models.IntegerField(blank=True,null=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255,blank=True,null=True)
    created_by = models.ForeignKey(User,related_name = 'orders',on_delete=models.SET_NULL,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    quantity = models.IntegerField(default=1)

    def get_display_price(self):
        return self.price / 100
    


