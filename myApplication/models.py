from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.FloatField()
	quantity = models.CharField(max_length=200)
	manufacturing_date = models.DateField()
	expiry_date = models.DateField()

	class Meta:
		app_label = 'myApplication'

	def __str__(self):
		return self.name