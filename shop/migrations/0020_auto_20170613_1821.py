# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-13 18:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopdata',
            name='subscription_expiry_date',
            field=models.DateTimeField(default=datetime.date(2017, 6, 13)),
        ),
    ]
