from django.db import models

class Cafe(models.Model):
	name = models.CharField(max_length=200)
	map_url = models.CharField(max_length=200)
	img_url = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	has_sockets = models.BooleanField()
	has_toilet = models.BooleanField()
	has_wifi = models.BooleanField()
	can_take_calls = models.BooleanField()
	seats = models.CharField(max_length=200)
	coffee_price = models.CharField(max_length=200)

	def __str__(self):
		return self.name