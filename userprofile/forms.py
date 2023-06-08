from django.forms import ModelForm
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter username...'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email Address...'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Enter password...'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirm password...'})



class UpdateProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

    def __init__(self,*args,**kwargs):
        super(UpdateProfileForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter Username...'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter First Name...'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter Last Name...'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email Address...'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Enter Password...'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Confirm Password...'})




