from django.urls import path
from . import consumers
websocket_urlpatterns = [
path(r'ws/echo/', consumers.EchoConsumer.as_asgi()),
]