# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-23 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='keys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=400, null=True)),
                ('value', models.CharField(blank=True, max_length=400, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
