from django import forms


class AddBook(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    rating = forms.CharField()
    