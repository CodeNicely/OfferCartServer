# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-09 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='wallet',
        ),
        migrations.AddField(
            model_name='userdata',
            name='fcm',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
