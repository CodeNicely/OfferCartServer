# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-19 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_data',
            name='image_url',
            field=models.ImageField(default='welcome/default.png', upload_to='welcome/'),
        ),
    ]
