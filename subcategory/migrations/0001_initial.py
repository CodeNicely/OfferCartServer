# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subcategory_data',
            fields=[
                ('subcategory_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_id', models.SmallIntegerField(default=0)),
                ('category_id', models.SmallIntegerField(default=0)),
                ('data_type', models.SmallIntegerField(default=3)),
                ('subcategory_name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
