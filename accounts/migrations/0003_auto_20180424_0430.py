# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-23 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180423_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='loan',
            field=models.DecimalField(decimal_places=2, default=10000.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='net_worth',
            field=models.DecimalField(decimal_places=2, default=models.DecimalField(decimal_places=2, default=10000.0, max_digits=20), max_digits=20),
        ),
    ]