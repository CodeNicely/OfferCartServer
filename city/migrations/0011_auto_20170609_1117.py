# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-09 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0010_auto_20170406_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cityfcmdata',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='cityfcmdata',
            name='user_id',
        ),
        migrations.AddField(
            model_name='citydata',
            name='state_id',
            field=models.IntegerField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='citydata',
            name='state_name',
            field=models.CharField(default='India', max_length=255),
        ),
        migrations.DeleteModel(
            name='CityFcmData',
        ),
    ]
