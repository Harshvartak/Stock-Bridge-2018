# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-28 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20180428_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='companycmprecord',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Company'),
            preserve_default=False,
        ),
    ]