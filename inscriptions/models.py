from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    name = models.TextField(max_length=255)
    personal_email = models.TextField(max_length=255)
    google_email = models.TextField(max_length=255)

class Paper(models.Model):
    author = models.ForeignKey(Author)
    title = models.TextField(max_length=255)
    summary = models.TextField(max_length=255)
    collaborators = models.TextField(max_length=255)
    topic = models.TextField(
        max_length=255,
        choices=[
            ('CLOUD', 'CLOUD'),
            ('SOA', 'SOA'),
            ('WS', 'WS'),
            ('BPM', 'BPM'),
        ]
    )
    presentation_type = models.TextField(
        max_length=255,
        choices=(
            ('poster', 'poster'),
            ('conferencia', 'conferencia'),
        )
    )
    state = models.TextField(
        max_length=255,
        choices=(
            ('unassigned', 'unassigned'),
            ('assigned', 'assigned'),
            ('accepted', 'accepted'),
            ('closed', 'closed'),
            ('finalized', 'finalized'),
        ),
        default='unassigned'
    )
    presentation_date = models.TextField(null=True)
    presentation_place = models.TextField(max_length=255, null=True)
    gdrive_id = models.TextField(max_length=255, null=True)
    gdrive_link = models.TextField(max_length=255, null=True)
    gdrive_content = models.TextField(max_length=255, null=True)
