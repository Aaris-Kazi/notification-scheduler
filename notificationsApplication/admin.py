from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User_Device)
class UserDeviceAdmin(admin.ModelAdmin):
    list_display = [
        'users',
        'device_type'
    ]
    search_fields = [
        'users'
    ]
    ordering = [
        'users'
    ]