from django.urls import re_path
from . import NotificationConsumers

websocket_urlpatterns = [
    # re_path(r'ws/notify/(?P<username>\w+)/$', NotificationConsumers.as_asgi())
    re_path(r'ws/notify/', NotificationConsumers.as_asgi())
]

