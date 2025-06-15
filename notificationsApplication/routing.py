from django.urls import re_path
from . import NotificationConsumers

websocket_url = [
    re_path(r'^ws/notify/(?P<username>\w+)/$', NotificationConsumers.as_asgi())
]

