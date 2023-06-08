from django.contrib import admin

from .models import Userprofile,User

# Register your models here.

admin.site.register(Userprofile)
admin.site.register(User)
