from django.db import models

# Create your models here.


class Players(models.Model):
	name = models.CharField(max_length=255)
	contact_no = models.CharField(max_length=10)
	address = models.TextField()
	age = models.IntegerField()
	category = models.CharField(max_length=255, help_text = 'Football Cricket etc')



	