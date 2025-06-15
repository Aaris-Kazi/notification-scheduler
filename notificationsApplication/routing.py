from django.urls import re_path
from . import NotificationConsumers

websocket_url = [
    re_path(r'ws/notify/(?P<user_id>\w+)/$', NotificationConsumers.as_asgi())
]

