# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-09 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='user', max_length=128),
        ),
    ]