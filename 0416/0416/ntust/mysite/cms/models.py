from django.db import models

class person(models.Model):
	name = models.CharField(max_length=10)
	birthday = models.CharField(max_length=10)
	is_girl = models.BooleanField(default=0)
	def __str__(self):
		return self.name


# Create your models here.
