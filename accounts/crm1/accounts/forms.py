from django.forms import ModelForm
from .models import Order
from .models import Customers
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Orderform(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class Customerform(ModelForm):
    class Meta:
        model=Customers
        fields='__all__'
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']