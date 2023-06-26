"""
ASGI config for taxi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from trips.consumers import TaxiConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taxi.settings")


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(
            [
                path("taxi/", TaxiConsumer.as_asgi()),
            ]
        ),
    }
)
