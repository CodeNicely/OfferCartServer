# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-12 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20161110_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='offers_bought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=120, null=True)),
                ('offer_id', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]