from django import forms

from .models import Product,Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name','last_name','email','address','zipcode','city',)

class ProductForm(forms.ModelForm):
    price = forms.DecimalField(decimal_places=2)

    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image', 'status',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'p-4 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'p-4 border border-gray-200'
            }),
            'description': forms.TextInput(attrs={
                'class': 'p-4 border border-gray-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'p-4 border border-gray-200'
            }),
            'status': forms.Select(attrs={
                'class': 'p-4 border border-gray-200'
            }),
        }
