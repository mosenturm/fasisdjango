# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponse
from django.utils import timezone

from django.core import serializers
from django.contrib.auth.decorators import login_required

from .forms import CustomerForm
from .models_1 import Customer

# Homepage mit dashboard
@login_required
def index(request):
    #reminders = Customer.objects.filter(reminder__gte=timezone.now()) # greater or equal
    reminders = Customer.objects.filter(reminder__gt='1970-01-01') # greater
    context = {'reminders': reminders,
               'datenow': timezone.now()
    }
    return render(request, 'core/home.html', context)

# edit reminder date
def reminder_edit(request, pk):
    #return render(request, 'core/home.html')
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
    