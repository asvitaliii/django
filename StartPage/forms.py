from django import forms
from .models import Verse, Author


class VerseForm(forms.ModelForm):
    class Meta:
        model = Verse
        fields = ('name', 'author', 'text')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'about')
