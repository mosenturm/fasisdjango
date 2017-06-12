# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-03 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('order_id', models.IntegerField()),
                ('file_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'attachments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField()),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('cust_id', models.IntegerField()),
            ],
            options={
                'db_table': 'notes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('cust_id', models.IntegerField()),
                ('order_type_id', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'order_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'persons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=11)),
                ('invoice_no', models.CharField(blank=True, max_length=60, null=True)),
                ('created', models.DateTimeField()),
                ('cust_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_email', models.CharField(max_length=255)),
                ('user_password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user_login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kategorie')),
            ],
            options={
                'verbose_name': 'Kunde Kategorie',
                'db_table': 'cust_categories',
                'managed': True,
                'verbose_name_plural': 'Kunden Kategorien',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=100, verbose_name='Name')),
                ('cust_contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Kontakt')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Stra\xdfe')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ort')),
                ('zip', models.CharField(blank=True, max_length=20, null=True, verbose_name='PLZ')),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('telefon', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='mobil')),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('reminder', models.DateField(default='1970-01-01', verbose_name='WV')),
                ('category', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='core.CustCategories')),
            ],
            options={
                'verbose_name': 'Kunde',
                'db_table': 'customer',
                'managed': True,
                'verbose_name_plural': 'Kunden',
            },
        ),
        migrations.CreateModel(
            name='CustTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kundentyp')),
            ],
            options={
                'verbose_name': 'Kunden Typ',
                'db_table': 'cust_types',
                'managed': True,
                'verbose_name_plural': 'Kunden Typen',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='type',
            field=models.ForeignKey(db_column='type_id', on_delete=django.db.models.deletion.CASCADE, to='core.CustTypes'),
        ),
    ]
