from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CartForm(forms.Form):
    quantity = forms.IntegerField(initial = '1')
    product_id = forms.IntegerField(widget = forms.HiddenInput
    )

    def __init__(self,request,*args,**kwargs):
        self.request = request
        super(CartForm,self).__init__(*args,**kwargs)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']