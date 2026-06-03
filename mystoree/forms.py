from django import forms
from .models import Customer,Monthly

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =['cname','cphoto','cphone','caddress']


class MonthlyForm(forms.ModelForm):
    class Meta:
        model = Monthly
        fields=['january','febraury','march','april','may','june','july','august','september','october','november','december']