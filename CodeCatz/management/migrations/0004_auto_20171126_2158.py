# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20171126_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hours',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
