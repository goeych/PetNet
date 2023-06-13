from django.shortcuts import render,redirect
import datetime
from django.db.models import Q

from .models import Equipment,Calibration,Department
from .forms import AddCalibrationRecordForm,UpdateCalibrationRecordForm

def equipmentPage(request):
    context={}

    return render(request,'equipment/equipmentpage.html',context)
    
    

def weeklymonitor(request):
    getdate = datetime.date.today()
    currentdate = getdate.strftime('%d %B %y')
    ListAll = Calibration.objects.all()
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    ##weeklymonitors = Calibration.objects.filter(Q(equipment__department__department=q),
      ##                                          Q(complete=False),
        ##                                        )

    weeklymonitors = Calibration.objects.filter(Q(department_fk__department__icontains=q) & Q(publish=True))


    departments = Department.objects.all() 
   # weeklymonitors = Equipment.objects.all()
    
    context={'weeklymonitors':weeklymonitors,
             'currentdate':currentdate,
             'departments':departments,}

    return render(request,'equipment/list.html',context)

def ListCalibrationRecord(request):
    calibrations = Calibration.objects.all()
    context ={'calibrations':calibrations}
    return render(request,'equipment/ListCalibrationRecord.html',context)

def AddCalibrationRecord(request):

    if request.method == 'POST':
        form = AddCalibrationRecordForm(request.POST,request.FILES)# Include request.FILES to handle file uploads

        if form.is_valid():
            form_data = form.save(commit =False)
            #department = form.cleaned_data['department']
            #equipment = form.cleaned_data['equipment_id']
            
            #Calibration.objects.create(department_fk = department,
                                       #equipment_fk = equipment,)

            form_data.attachment = request.FILES.get('attachment')
            form_data.save()
      
            
            return redirect('weeklymonitor')
        else:
            print('error:',form.errors)
    else:
        form = AddCalibrationRecordForm()
        
    context ={'form':form}
    return render(request,'equipment/AddCalibrationRecordForm.html',context)

def UpdateCalibrationRecord(request,pk):
    UpdateEquipmentRecord = Calibration.objects.get(id=pk)
    form = UpdateCalibrationRecordForm()

    if request.method == 'POST':
        form = UpdateCalibrationRecordForm(request.POST,instance = UpdateEquipmentRecord)

        if form.is_valid():
            form.save()
            return redirect('weeklymonitor')
        else:
            print('error:',form.errors)
    else:
        print('request not post')
        form = AddCalibrationRecordForm(instance = UpdateEquipmentRecord)
        
    context ={'form':form}
    return render(request,'equipment/UpdateCalibrationRecordForm.html',context)
    
def DeleteCalibrationRecord(request,pk):
    DeleteEquipmentRecord = Calibration.objects.get(id=pk)

    
    if request.method == 'POST':
        DeleteEquipmentRecord.delete()
        return redirect('weeklymonitor')
    
    context ={}
    return render(request,'equipment/DeleteCalibrationRecordForm.html',context)
        
        

    
    
    
    
    

