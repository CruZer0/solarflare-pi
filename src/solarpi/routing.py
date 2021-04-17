import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.conf.urls import url
from tcore.consumers import TempConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
            URLRouter(
                [
                    url('', TempConsumer.as_asgi())
                ]
            )
        )
})