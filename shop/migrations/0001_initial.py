# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shop_data',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_id', models.SmallIntegerField(default=0)),
                ('category_id', models.SmallIntegerField(default=0)),
                ('shop_name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
