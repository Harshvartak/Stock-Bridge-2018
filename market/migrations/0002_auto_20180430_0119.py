# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-29 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['cap_type', 'code']},
        ),
    ]
