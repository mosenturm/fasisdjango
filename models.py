# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Attachments(models.Model):
    description = models.TextField()
    order_id = models.IntegerField()
    file_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'


class CustCategories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cust_categories'


class CustTypes(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cust_types'


class Customer(models.Model):
    cust_name = models.CharField(max_length=100)
    cust_contact = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    category_id = models.IntegerField()
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer'


class Notes(models.Model):
    header = models.TextField()
    content = models.TextField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    cust_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notes'


class OrderType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'order_type'


class Orders(models.Model):
    description = models.TextField()
    cust_id = models.IntegerField()
    order_type_id = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders'


class Persons(models.Model):
    name = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class Sales(models.Model):
    value = models.DecimalField(max_digits=11, decimal_places=2)
    invoice_no = models.CharField(max_length=60, blank=True, null=True)
    created = models.DateTimeField()
    cust_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales'


class UserLogin(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_login'
