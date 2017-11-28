# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
        ('events', '0011_auto_20171125_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ManyToManyField(blank=True, help_text='Assign employee to event', to='events.Event')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='register.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('COOOK', 'COOK'), ('WAITER', 'WAITER'), ('DELIVERY', 'DELIVERY')], help_text='Choose role', max_length=15, null=True, unique=True)),
            ],
        ),
    ]
