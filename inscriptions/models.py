from __future__ import unicode_literals

from django.db import models

class Paper(models.Model):
    title = models.TextField(max_length=255)
    summary = models.TextField(max_length=255)
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
            ('assigned', 'assigned'),
            ('accepted', 'accepted'),
            ('closed', 'closed'),
            ('finalized', 'finalized'),
        )
    )
    presentation_date = models.DateTimeField()

class Author(models.Model):
    name = models.TextField(max_length=255)
    personal_email = models.EmailField()
    google_email = models.EmailField()
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    is_collaborator = models.BooleanField(default=False)


