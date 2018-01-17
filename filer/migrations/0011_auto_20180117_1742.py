# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-17 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_file_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filename',
            field=models.UUIDField(blank=True, default=None, help_text='Not used at the moment', null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='uuid',
            field=models.UUIDField(blank=True, default=None, help_text='Unique identifier for an asset. Base of the file name in the API', null=True),
        ),
    ]
