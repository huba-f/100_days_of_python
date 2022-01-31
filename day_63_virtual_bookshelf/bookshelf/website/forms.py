from ast import Add
from django import forms
from .models import AddBook

class AddBookForm(forms.ModelForm):
    class Meta:
        model = AddBook
        fields = ['title', 'author', 'rating']
