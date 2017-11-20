# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0030_auto_20171119_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('COOOK', 'COOK'), ('WAITER', 'WAITER'), ('DELIVERY', 'DELIVERY')], help_text='Choose role', max_length=15, null=True, unique=True),
        ),
    ]
