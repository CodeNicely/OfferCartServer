# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_remove_offer_data_data_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer_data',
            name='validity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]