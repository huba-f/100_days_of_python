from django.db import models

# Create your models here.
class AddMovie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    ranking = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title + " " + self.year
        