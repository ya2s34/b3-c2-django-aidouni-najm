from django import forms
from .models import Site

class FormSite(forms.ModelForm):
    class Meta:
        model = Site
        fields = ('nom', 'url', 'description', 'identifiant', 'password')