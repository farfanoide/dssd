# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0005_auto_20161114_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='presentation_place',
            field=models.CharField(max_length=255, null=True),
        ),
    ]