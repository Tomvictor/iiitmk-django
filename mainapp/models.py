from django.db import models
from django.utils import timezone
# Create your models here.



class Device(models.Model):
	name = models.CharField(max_length=100)
	imei = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class LocationHistory(models.Model):
	timestamp = models.DateTimeField(default=timezone.now())
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
	device = models.ForeignKey(Device, on_delete= models.CASCADE)

	def __str__(self):
		return str(self.timestamp)
