# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-03 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myoffers', '0002_auto_20161103_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer_bought_data',
            name='transaction_id',
            field=models.IntegerField(default=0),
        ),
    ]
