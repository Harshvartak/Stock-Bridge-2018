# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-26 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('cap', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('stocks_offered', models.IntegerField(default=0)),
                ('stocks_remaining', models.IntegerField(default=models.IntegerField(default=0))),
                ('cmp', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
