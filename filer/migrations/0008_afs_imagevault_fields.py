# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-12 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='iv_album_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='album id'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_file_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='file id'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_file_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='file name'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_author',
            field=models.CharField(blank=True, max_length=255, verbose_name='auteur'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_byline_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='byline title'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_caption_writer',
            field=models.CharField(blank=True, max_length=255, verbose_name='caption writer'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_city',
            field=models.CharField(blank=True, max_length=255, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_compression',
            field=models.CharField(blank=True, max_length=255, verbose_name='compression'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_contact',
            field=models.CharField(blank=True, max_length=255, verbose_name='contact'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_country',
            field=models.CharField(blank=True, max_length=255, verbose_name='country'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_credit_line',
            field=models.CharField(blank=True, max_length=255, verbose_name='credit line'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_date_created',
            field=models.CharField(blank=True, max_length=255, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_date_from_category',
            field=models.CharField(blank=True, max_length=255, verbose_name='date from category'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_date_time_created',
            field=models.CharField(blank=True, max_length=255, verbose_name='date time created'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_description',
            field=models.TextField(blank=True, verbose_name='beschrijving'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_description_long',
            field=models.TextField(blank=True, verbose_name='description long'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_duration',
            field=models.CharField(blank=True, max_length=255, verbose_name='duration'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_headline',
            field=models.TextField(blank=True, verbose_name='headline'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_instructions',
            field=models.CharField(blank=True, max_length=255, verbose_name='instructions'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_job_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='job id'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_keywords',
            field=models.CharField(blank=True, max_length=840, verbose_name='keywords'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_orientation',
            field=models.CharField(blank=True, max_length=255, verbose_name='orientation'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_original_filename',
            field=models.CharField(blank=True, max_length=255, verbose_name='oorspronkelijke bestandsnaam'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_province',
            field=models.CharField(blank=True, max_length=255, verbose_name='province'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_rights_usage_terms',
            field=models.CharField(blank=True, max_length=255, verbose_name='rights usage terms'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_source',
            field=models.CharField(blank=True, max_length=255, verbose_name='source'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_status_online',
            field=models.CharField(blank=True, max_length=255, verbose_name='status online'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_sub_location',
            field=models.CharField(blank=True, max_length=255, verbose_name='sub location'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_metadata_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='titel'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='naam'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_page_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='page id'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_page_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='page name'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_page_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='page title'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_page_url',
            field=models.CharField(blank=True, max_length=320, verbose_name='page url'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_path',
            field=models.CharField(blank=True, max_length=255, verbose_name='path'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='titel'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_user_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='user name'),
        ),
        migrations.AddField(
            model_name='file',
            name='iv_user_name2',
            field=models.CharField(blank=True, max_length=255, verbose_name='user name2'),
        ),
    ]
