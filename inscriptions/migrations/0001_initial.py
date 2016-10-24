# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('personal_email', models.EmailField(max_length=254)),
                ('google_email', models.EmailField(max_length=254)),
                ('is_collaborator', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('summary', models.TextField(max_length=255)),
                ('topic', models.TextField(choices=[('cloud', 'cloud'), ('soa', 'soa'), ('ws', 'ws'), ('bpm', 'bpm')], max_length=255)),
                ('presentation_type', models.TextField(choices=[('poster', 'poster'), ('conferencia', 'conferencia')], max_length=255)),
                ('state', models.TextField(choices=[('assigned', 'assigned'), ('accepted', 'accepted'), ('closed', 'closed'), ('finalized', 'finalized')], max_length=255)),
                ('presentation_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscriptions.Paper'),
        ),
    ]
