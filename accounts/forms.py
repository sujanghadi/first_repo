from django.forms import ModelForm
from .models import Order
from .models import Customers

class Orderform(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class Customerform(ModelForm):
    class Meta:
        model=Customers
        fields='__all__'