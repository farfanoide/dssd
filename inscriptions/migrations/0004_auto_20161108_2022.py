# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0003_auto_20161108_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='topic',
            field=models.TextField(choices=[('CLOUD', 'CLOUD'), ('SOA', 'SOA'), ('WS', 'WS'), ('BPM', 'BPM')], max_length=255),
        ),
    ]
