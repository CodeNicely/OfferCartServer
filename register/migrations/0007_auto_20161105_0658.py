# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_user_data_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_data',
            name='mobile',
            field=models.CharField(blank=True, default='7587485272', max_length=120, null=True),
        ),
    ]
