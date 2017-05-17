# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-12 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170331_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopdata',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='shopdata',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]