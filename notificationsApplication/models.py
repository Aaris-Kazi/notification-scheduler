from datetime import datetime
from django.db import models

from constants.AppConstants import DEVICE_TYPE_CHOICES, DEFAULT_DEVICE_TYPE_CHOICES


# Create your models here.

class User_Device(models.Model):
    users = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50, blank=True)
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES, default=DEFAULT_DEVICE_TYPE_CHOICES)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.users
    
