# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(help_text='Up to 15 digits allowed.', max_length=15, null=True),
        ),
    ]