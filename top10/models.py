from django.db import models

# Create your models here.
class Album(models.Model):
	name=models.CharField(max_length=50)
	artist=models.CharField(max_length=50)
	link=models.URLField()