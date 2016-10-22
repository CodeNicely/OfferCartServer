# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-22 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp_data',
            name='id',
        ),
        migrations.AlterField(
            model_name='otp_data',
            name='flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='otp_data',
            name='mobile',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, primary_key=True, serialize=False),
        ),
    ]
