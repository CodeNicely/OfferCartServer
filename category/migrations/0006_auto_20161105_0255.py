# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20161023_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_data',
            name='image',
            field=models.ImageField(default='/media/category/default.png', upload_to='category/'),
        ),
    ]