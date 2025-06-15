from django.urls import include, path
from rest_framework import routers

from .views import NotificationViewsets, DeviceViewsets

router = routers.DefaultRouter()
router.register('notification', NotificationViewsets, basename='notification')
router.register('device', DeviceViewsets, basename='device')


urlpatterns = [
    path('', include(router.urls)),
]