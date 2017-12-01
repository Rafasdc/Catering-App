# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_auto_20171201_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventInventoryInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'verbose_name': 'Event Inventory',
                'verbose_name_plural': 'Event Inventories',
            },
        ),
        migrations.CreateModel(
            name='EventQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Amount necessary for event.')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.EventInventoryInstance')),
            ],
            options={
                'verbose_name': 'Event Quantity',
                'verbose_name_plural': 'Event Quantities',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of Item')),
                ('description', models.CharField(blank=True, max_length=64, null=True, verbose_name='Description')),
                ('part_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Item number')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='ItemInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountAvailable', models.IntegerField(verbose_name='Amount Available in Inventory')),
                ('amountUnavailable', models.IntegerField(verbose_name='Amount Used from Inventory')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
            ],
            options={
                'verbose_name': 'Item inventory',
                'verbose_name_plural': 'Item inventories',
            },
        ),
        migrations.AddField(
            model_name='eventquantity',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item'),
        ),
        migrations.AddField(
            model_name='eventinventoryinstance',
            name='items',
            field=models.ManyToManyField(through='inventory.EventQuantity', to='inventory.Item'),
        ),
    ]
