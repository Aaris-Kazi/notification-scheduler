"""
ASGI config for notifyx project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from notificationsApplication.routing import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack
from loggings.CustomLogging import logger

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifyx.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        )
})

logger.info("ASGI init")