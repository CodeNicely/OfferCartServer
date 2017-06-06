# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 11:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0004_auto_20170518_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerdata',
            name='price',
        ),
        migrations.AlterField(
            model_name='offerdata',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2017, 5, 19)),
        ),
    ]
