from django.contrib import admin

from .models import Department,Equipment,Calibration

# Register your models here.

admin.site.register(Department)
admin.site.register(Calibration)
admin.site.register(Equipment)
