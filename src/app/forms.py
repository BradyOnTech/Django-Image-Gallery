from django import forms
from app.models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    file = forms.FileField()