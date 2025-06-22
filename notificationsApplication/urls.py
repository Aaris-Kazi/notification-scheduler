from django.urls import include, path
from rest_framework import routers

from .views import NotificationViewsets, DeviceViewsets, NotificationViewsetsV2

router = routers.DefaultRouter()
router.register('v1/notification', NotificationViewsets, basename='notification')
router.register('v2/notification', NotificationViewsetsV2, basename='notificationv2')
router.register('v1/device', DeviceViewsets, basename='device')


urlpatterns = [
    path('', include(router.urls)),
]