from django import forms
from inscriptions.models import Paper
from crispy_forms.helper import FormHelper


class PaperForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PaperForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    author_name = forms.CharField(max_length=255)
    author_personal_email = forms.EmailField()
    author_google_email = forms.EmailField()

    paper_collaborators = forms.CharField(widget=forms.TextInput(attrs={'class': 'tags'}), max_length=255)
    paper_title = forms.CharField(max_length=255)
    paper_summary = forms.CharField(widget=forms.Textarea, max_length=255)
    paper_topic = forms.ChoiceField(
        choices=[
            ('CLOUD', 'CLOUD'),
            ('SOA', 'SOA'),
            ('WS', 'WS'),
            ('BPM', 'BPM'),
        ]
    )
    paper_presentation_type = forms.ChoiceField(
        choices=(
            ('Poster', 'Poster'),
            ('Conferencia', 'Conferencia'),
        )
    )

