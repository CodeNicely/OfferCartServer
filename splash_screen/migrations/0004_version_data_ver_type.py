# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash_screen', '0003_auto_20161012_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='version_data',
            name='ver_type',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
