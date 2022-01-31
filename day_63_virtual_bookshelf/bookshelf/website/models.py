from django.db import models

# Create your models here.
class AddBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return self.title + " by " + self.author