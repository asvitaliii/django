from django import forms
from .models import Verse


class VerseForm(forms.ModelForm):
    class Meta:
        model = Verse
        fields = ('name', 'author', 'text')
