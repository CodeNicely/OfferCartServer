# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-23 11:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20161023_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_data',
            name='created',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 10, 23, 11, 11, 18, 938810, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop_data',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 10, 23, 11, 11, 20, 734314, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
