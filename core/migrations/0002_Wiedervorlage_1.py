# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-03 13:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_Wiedervorlage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='reminder',
        ),
    ]
