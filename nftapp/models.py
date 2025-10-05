
from django.db import models

class NFTRelease(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	launch_date = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.name
