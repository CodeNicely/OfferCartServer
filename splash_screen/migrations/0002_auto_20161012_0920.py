# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splash_screen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version_control',
            old_name='version_no',
            new_name='version',
        ),
    ]
