from .models import Equipment,Calibration,Department
from django.forms import ModelForm

from django import forms
from django.db import models
from django.forms import widgets

class AddCalibrationRecordForm(forms.ModelForm):
    attachment = forms.FileField(label='Attachment', required=False)  # Add this field for the attachment
    
    class Meta:
        model = Calibration
        fields = ['department_fk','equipment_fk','last_cal','due_cal','complete','publish','remark','attachment'] # Add other fields here

        widgets = {
            'last_cal': forms.DateInput(attrs={'class': 'datepicker form-control', 'placeholder': 'Enter Cal date...'}),
            'due_cal': forms.DateInput(attrs={'class': 'datepicker form-control', 'placeholder': 'Enter Due date...'}),
            # Add widget configurations for other fields if needed
        }
        


    def __init__(self,*args,**kwargs):
        super(AddCalibrationRecordForm,self).__init__(*args,**kwargs)
        self.fields['department_fk'].widget.attrs.update({'class':'form-control','placeholder':'Choice Dept...'})
        self.fields['equipment_fk'].widget.attrs.update({'class':'form-control','placeholder':'Choice ID...'})
        self.fields['last_cal'].widget.attrs.update({'class': 'datepicker form-control', 'placeholder': 'Enter Cal date...'})
        self.fields['due_cal'].widget.attrs.update({'class': 'datepicker form-control', 'placeholder': 'Enter Due date...'})
        self.fields['complete'].widget.attrs.update({'class':'form-control','placeholder':'Complete...'})
        self.fields['publish'].widget.attrs.update({'class':'form-control','placeholder':'Publish ...'})
        self.fields['remark'].widget.attrs.update({'class':'form-control','placeholder':'Remark...'})


class UpdateCalibrationRecordForm(forms.ModelForm):
    class Meta:
        model = Calibration
        fields = ['department_fk','equipment_fk','last_cal','due_cal','complete','publish','remark',] # Add other fields here

        widgets = {
            'last_cal': forms.DateInput(attrs={'class': 'datepicker form-control', 'placeholder': 'Enter Cal date...'}),
            'due_cal': forms.DateInput(attrs={'class': 'datepicker form-control', 'placeholder': 'Enter Due date...'}),
            # Add widget configurations for other fields if needed
        }
        


    def __init__(self,*args,**kwargs):
        super(UpdateCalibrationRecordForm,self).__init__(*args,**kwargs)
        self.fields['department_fk'].widget.attrs.update({'class':'form-control','placeholder':'Choice Dept...'})
        self.fields['equipment_fk'].widget.attrs.update({'class':'form-control','placeholder':'Choice ID...'})
        self.fields['last_cal'].widget.attrs.update({'class': 'datepicker form-control', 'placeholder': 'Enter Cal date...'})
        self.fields['due_cal'].widget.attrs.update({'class': 'datepicker form-control', 'placeholder': 'Enter Due date...'})
        self.fields['complete'].widget.attrs.update({'class':'form-control','placeholder':'Complete...'})
        self.fields['publish'].widget.attrs.update({'class':'form-control','placeholder':'Publish ...'})
        self.fields['remark'].widget.attrs.update({'class':'form-control','placeholder':'Remark...'})
        

        
