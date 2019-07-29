from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Album(models.Model):
	name=models.CharField(max_length=50)
	artist=models.CharField(max_length=50)
	link=models.URLField()

class UserInfo(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	picture=models.ImageField(blank=True,upload_to='profile_pics')