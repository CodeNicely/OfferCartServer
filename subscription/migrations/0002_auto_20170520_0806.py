# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-20 08:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriptiondata',
            old_name='subscription_name',
            new_name='subscription_title',
        ),
    ]
