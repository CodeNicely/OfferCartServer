# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-06 09:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_auto_20170605_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdata',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2017, 6, 6)),
        ),
    ]