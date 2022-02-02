from django import forms
from .models import AddMovie

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = AddMovie
        fields = ['title', 'year', 'description', 'rating', 'ranking', 'review', 'img_url']