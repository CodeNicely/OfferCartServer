# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20161101_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_data',
            name='image',
            field=models.ImageField(default='/media/shop/default.png', upload_to='shop/'),
        ),
    ]
