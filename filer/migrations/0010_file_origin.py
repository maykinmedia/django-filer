# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-17 14:45
from __future__ import unicode_literals

from django.db import migrations, models

from ..choices import OriginChoices


def populate_origin(apps, schema_editor):
    File = apps.get_model('filer', 'File')

    for f in File.objects.all():
        if f.uuid:
            f.origin = OriginChoices.memorix
        elif f.iv_file_id:
            f.origin = OriginChoices.image_vault
        f.save()


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0009_afs_memorix_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='origin',
            field=models.CharField(choices=[('uploaded', 'Uploaded'), ('memorix', 'Memorix'), ('image_vault', 'Image Vault')], default='uploaded', max_length=20, verbose_name='Origin'),
        ),

        migrations.RunPython(populate_origin, migrations.RunPython.noop),
    ]