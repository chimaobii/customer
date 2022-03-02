from dataclasses import field, fields
from django import forms
from pages.models import customers 

class addform(forms.ModelForm):
    class Meta:
        model = customers
        fields = ['first_name', 'last_name', 'email', 'phone']