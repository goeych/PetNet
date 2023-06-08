from django.db import models
from datetime import datetime
from django import forms

# Create your models here.



class Department (models.Model):
    department = models.CharField(max_length = 200)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department

class Equipment(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    equipment_id = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    status = models.IntegerField(null=True,blank=True)
    #cal_item = models.CharField(max_length = 255)
    #ref_standard = models.CharField(max_length=200,null=True,blank=True)
    #nist_no = models.CharField(max_length=50,null=True,blank=True)
    serial_no = models.CharField(max_length=50,null=True,blank=True)
    #asset_no = models.CharField(max_length=50,null=True,blank=True)
    model_no = models.CharField(max_length=50,null=True,blank=True)
    #caltype = models.CharField(max_length=50,null=True,blank=True)
    #email = models.EmailField(null=True,blank=True)
    #unit_of_meas = models.CharField(max_length=50,null=True,blank=True)
    #drawing_no = models.CharField(max_length=50,null=True,blank=True)
    #drawing_date = models.CharField(max_length=50,null=True,blank=True)
    remarks = models.TextField(null=True,blank=True)
    storage_location = models.CharField(max_length=50,null=True,blank=True)
    #current_location = models.CharField(max_length=50,null=True,blank=True)
    #service_date = models.DateTimeField(null=True,blank=True)
    #retirement_date = models.DateTimeField(null=True,blank=True)
    #supplier_code = models.CharField(max_length=50,null=True,blank=True)
    #cost = models.FloatField(null=True,blank=True)
    #purchase_date = models.DateTimeField(null=True,blank=True)
    #user_defined = models.TextField(null=True,blank=True)
    manufacturer = models.CharField(max_length=50,null=True,blank=True)
    owner = models.CharField(max_length=50,null=True,blank=True)
    #vendor_contact = models.CharField(max_length=50,null=True,blank=True)
    cal_item = models.CharField(max_length=50,null=True,blank=True)
    cal_type = models.CharField(max_length=50,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.equipment_id}"

# for calibration
class Calibration(models.Model):
    department_fk = models.ForeignKey(Department,related_name='calibrations',verbose_name = 'Department',on_delete=models.SET_NULL,null=True,blank=True)
    equipment_fk = models.ForeignKey(Equipment,related_name='calibrations',verbose_name='Equipment ID',on_delete=models.SET_NULL,null=True,blank=True)
    #equipment_id = models.CharField(max_length=50,null=True,blank=True)
    #department = models.CharField(max_length=50,null=True,blank=True)
    last_cal = models.DateField()
    due_cal = models.DateField()
    #last_cal = models.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #due_cal = models.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    complete = models.BooleanField(default=False)
    publish = models.BooleanField(default=True)
    remark = models.TextField(null=False,blank=False)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)  # Field for PDF attachment
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_difference(self):
        difference = self.due_cal - self.last_cal
        return difference.days

    def get_remain(self):
        today = datetime.today().date()
        remain = self.due_cal - today
        return remain.days
        

    def __str__(self):
        return f"{self.equipment_fk}"

    class Meta:
        ordering = ('due_cal',)

 
class WeeklyMonitor(models.Model):
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE)
    
    #equipment_id  = models.CharField(max_length=255)
    #description  = models.TextField(null=False,blank=False)
    #cal_item = models.CharField(max_length = 255)
    #status =  models.IntegerField()
   # serial_no = models.CharField(max_length=255)
   # model_no= models.CharField(max_length=255)
   # manufacturer = models.CharField(max_length=255)

    
   

    

