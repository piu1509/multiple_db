from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=255)
	roll_no = models.IntegerField()
	department = models.CharField(max_length=200)
	year = models.CharField(max_length=10)

	class Meta:
		app_label = 'myApp'

	def __str__(self):
		return self.name+self.department


class Teacher(models.Model):
	name = models.CharField(max_length=255)
	staff_id = models.IntegerField()
	department = models.CharField(max_length=200)

	class Meta:
		app_label = 'myApp'

	def __str__(self):
		return self.name+self.department