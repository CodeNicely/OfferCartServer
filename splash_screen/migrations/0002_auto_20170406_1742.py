# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splash_screen', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FcmData',
        ),
        migrations.DeleteModel(
            name='VersionData',
        ),
    ]