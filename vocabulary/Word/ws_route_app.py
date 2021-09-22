from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from .consumer import WordConsumer
from django.urls import re_path

application = ProtocolTypeRouter({

    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r'swagger$', WordConsumer.as_asgi()),
        ])
    ),

})


