# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_offer_data_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer_data',
            old_name='describ',
            new_name='description',
        ),
    ]
