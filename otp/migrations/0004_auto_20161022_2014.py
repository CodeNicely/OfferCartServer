# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-22 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0003_auto_20161022_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_token_data',
            name='access_token',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
