# -*- coding: utf-8 -*-

# Forms for the customer handling
from django.forms import ModelForm, Form, DateField
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError

from tinymce.widgets import TinyMCE

import datetime #for checking renewal date range.

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
            'reminder': DateInput(attrs={'class': 'datepicker'}),
        }
        #exclude = ('date_created', 'date_updated', 'owner')
        
class RenewReminderForm(Form):
    renewal_date = DateField(label='Wiedervorlage am: ', help_text="Ein Datum größer als das aktuelle Datum eingeben.")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        #Check date is not in past. 
        if data < datetime.date.today():
            raise ValidationError('Falsches Datum - WV in der Vergangenheit')

        # Remember to always return the cleaned data.
        return data