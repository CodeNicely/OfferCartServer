# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-08 09:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0016_auto_20170613_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdata',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2017, 7, 8)),
        ),
    ]
