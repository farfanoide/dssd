from django import forms

class GdriveShareForm(forms.Form):

    user_email = forms.EmailField(
        label='Email del usuario',
        widget=forms.EmailInput({'class':'form-control'})
    )

class ClosePaperForm(forms.Form):
    pass
