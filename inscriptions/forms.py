from django import forms
from inscriptions.models import Paper


class PaperForm(forms.Form):
    form_tag = False

    author_name = forms.CharField(max_length=255)
    author_personal_email = forms.EmailField()
    author_google_email = forms.EmailField()

    paper_collaborators = forms.CharField(widget=forms.TextInput(attrs={'class': 'tags'}), max_length=255)
    paper_title = forms.CharField(max_length=255)
    paper_summary = forms.CharField(widget=forms.Textarea, max_length=255)
    paper_topic = forms.ChoiceField(
        choices=[
            ('cloud', 'cloud'),
            ('soa', 'soa'),
            ('ws', 'ws'),
            ('bpm', 'bpm'),
        ]
    )
    paper_presentation_type = forms.ChoiceField(
        choices=(
            ('poster', 'poster'),
            ('conferencia', 'conferencia'),
        )
    )
