# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-13 12:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0013_auto_20170610_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdata',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2017, 6, 13)),
        ),
    ]