# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_detectorupload_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectorupload',
            name='designation',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AddField(
            model_name='detectorupload',
            name='username',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
