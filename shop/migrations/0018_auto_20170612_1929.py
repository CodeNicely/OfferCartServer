# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-12 19:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20170610_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopdata',
            name='subscription_expiry_date',
            field=models.DateTimeField(default=datetime.date(2017, 6, 12)),
        ),
    ]
