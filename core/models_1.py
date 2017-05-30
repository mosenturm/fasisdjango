# -*- coding: utf-8 -*-

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
    name = models.CharField(max_length=100, verbose_name='Kategorie')

    class Meta:
        managed = True
        db_table = 'cust_categories'
        verbose_name = 'Kunde Kategorie'
        verbose_name_plural = 'Kunden Kategorien'
        
    def __unicode__(self):
        return "%s" % self.name

class CustTypes(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kundentyp')

    class Meta:
        managed = True
        db_table = 'cust_types'
        verbose_name = 'Kunden Typ'
        verbose_name_plural = 'Kunden Typen'

    def __unicode__(self):
        return "%s" % self.name

class Customer(models.Model):
    cust_name = models.CharField(max_length=100, verbose_name='Name')
    cust_contact = models.CharField(max_length=100, blank=True, null=True, verbose_name='Kontakt')
    street = models.CharField(max_length=100, blank=True, null=True, verbose_name='Straße')
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ort')
    zip = models.CharField(max_length=20, blank=True, null=True, verbose_name='PLZ')
    email = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='mobil')
    fax = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    category = models.ForeignKey(CustCategories, db_column='category_id')
    type = models.ForeignKey(CustTypes, db_column='type_id')

    class Meta:
        managed = True
        db_table = 'customer'
        verbose_name = 'Kunde'
        verbose_name_plural = 'Kunden'

    def __unicode__(self):
        return "%s" % self.cust_name


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
