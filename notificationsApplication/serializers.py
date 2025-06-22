from rest_framework import serializers
from constants.AppConstants import DEVICE_TYPE_CHOICES_SERIALIZER

class UserDevicesCreate(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    deviceType = serializers.ChoiceField(choices=DEVICE_TYPE_CHOICES_SERIALIZER)
    # deviceid = serializers.CharField(max_length=50)

class UserDevicesGet(serializers.Serializer):
    username = serializers.CharField(max_length=50)

class NotifictionCounter(serializers.Serializer):
    counter = serializers.IntegerField(default=0)

class NotifictionPopUp(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    deviceType = serializers.ChoiceField(choices=DEVICE_TYPE_CHOICES_SERIALIZER)
    deviceid = serializers.CharField(max_length=50)
    project_name = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=50, default="test")
    body = serializers.CharField(max_length=200, default="test")


class NotifictionPopUpV2(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    deviceType = serializers.ListField(child= serializers.ChoiceField(choices=DEVICE_TYPE_CHOICES_SERIALIZER), allow_empty= False)
    deviceid = serializers.CharField(max_length=50)
    project_name = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=50, default="test")
    body = serializers.CharField(max_length=200, default="test")

class NotifictionTriggerEvent(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    deviceType = serializers.ChoiceField(choices=DEVICE_TYPE_CHOICES_SERIALIZER)
    # deviceid = serializers.CharField(max_length=50)
    eventName = serializers.CharField(max_length=50)
