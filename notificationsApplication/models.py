from django.db import models

from constants.AppConstants import DEVICE_TYPE_CHOICES, DEFAULT_DEVICE_TYPE_CHOICES


# Create your models here.

class User_Device(models.Model):
    users = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES, default=DEFAULT_DEVICE_TYPE_CHOICES)

    def __str__(self):
        return self.users
    
