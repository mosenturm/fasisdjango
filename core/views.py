# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponse
from django.utils import timezone

from django.core import serializers
from django.contrib.auth.decorators import login_required

import datetime

from .forms import CustomerForm, RenewReminderForm
from .models_1 import Customer

# Homepage mit dashboard
@login_required
def index(request):
    #reminders = Customer.objects.filter(reminder__gte=timezone.now()) # greater or equal
    reminders = Customer.objects.filter(reminder__gt='1970-01-01') # greater
    context = {'reminders': reminders,
               'datenow': timezone.now(),
    }
    return render(request, 'core/home.html', context)

# edit reminder date
@login_required
def renew_reminder(request, pk):
    cust_inst=get_object_or_404(Customer, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewReminderForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model reminder field)
            cust_inst.reminder = form.cleaned_data['renewal_date']
            cust_inst.save()

            # redirect to a new URL:
            return redirect('home')

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewReminderForm(initial={'renewal_date': proposed_renewal_date,})
        
    return render(request, 'core/form_reminder.html', {'form': form, 'custinst':cust_inst})
    
# edit reminder date
@login_required
def reset_reminder(request, pk):
    cust_inst=get_object_or_404(Customer, pk = pk)

    # If this is a GET request then reset reminder for given pk
    if request.method == 'GET':
        cust_inst.reminder = '1970-01-01'
        cust_inst.save()
    return redirect('home')

# for testing
@login_required
def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'core/customer_list.html', context)

# AJAX JSON response for DataTable
@login_required
def get_customers(request):
    customer = Customer.objects.all().select_related("category").select_related("type")
    response = serializers.serialize("json", customer)
    return HttpResponse(response, content_type='application/json')

# main view for customertable, calls JSON data
@login_required
def customer_table(request):
    return render(request, 'core/customer_datatable.html')
    
@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(instance=customer, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_table')
    else:
        form = CustomerForm(instance=customer)
    context = {'form': form, 'create': False}
    return render(request, 'core/form.html', context)

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            #customer.owner = request.user
            customer.save()
            #form.save_m2m()
            return redirect('customer_table')
    else:
        form = CustomerForm()
    context = {'form': form, 'create': True}
    return render(request, 'core/form.html', context)

@login_required
def customer_delete(request, pk):                
    result=Customer.objects.get(pk=pk).delete()                              
    return redirect('customer_table')
    