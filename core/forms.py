# -*- coding: utf-8 -*-

# Forms for the customer handling
from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from .models_1 import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['cust_name', 
                  'cust_contact', 
                  'street', 
                  'city', 
                  'zip', 
                  'email', 
                  'website', 
                  'telefon', 
                  'mobile_phone', 
                  'fax', 
                  'note',
                  'reminder',
                  'category', 
                  'type']
        widgets = {
            'note': TinyMCE(attrs={'cols': 80, 'rows': 10}),
        }
        #exclude = ('date_created', 'date_updated', 'owner')