# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 09:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_auto_20170518_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdata',
            name='expiry_date',
            field=models.DateField(default=datetime.date(2017, 5, 18)),
        ),
    ]