# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-22 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='mobile',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]