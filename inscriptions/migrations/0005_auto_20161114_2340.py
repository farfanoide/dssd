# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0004_auto_20161108_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='gdrive_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='gdrive_link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]