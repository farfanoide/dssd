from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    name = models.TextField(max_length=255)
    personal_email = models.EmailField()
    google_email = models.EmailField()

class Paper(models.Model):
    author = models.ForeignKey(Author)
    title = models.TextField(max_length=255)
    summary = models.TextField(max_length=255)
    collaborators = models.TextField(max_length=255)
    link = models.TextField(max_length=255)
    topic = models.TextField(
        max_length=255,
        choices=[
            ('cloud', 'cloud'),
            ('soa', 'soa'),
            ('ws', 'ws'),
            ('bpm', 'bpm'),
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
    presentation_date = models.DateTimeField(null=True)
