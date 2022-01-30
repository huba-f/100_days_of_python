from django.db import models
from django.forms import ModelForm

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.author

    def __str__(self):
        return self.rating
