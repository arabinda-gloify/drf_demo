from django.db import models

# Create your models here.

class Mobile(models.Model):
	brand = models.CharField(max_length=255, blank=True, null=True)
	model_no = models.CharField(max_length=255, blank=True, null=True)
	ram = models.IntegerField(help_text='GB')
	rom = models.IntegerField(help_text='GB')
	screen = models.FloatField(help_text='inch')
	front_camera = models.IntegerField(help_text="MegaPixels")
	rear_camera = models.IntegerField(help_text="MegaPixels")