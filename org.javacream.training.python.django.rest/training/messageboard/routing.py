from django.urls import re_path
from . import consumers
websocket_urlpatterns = [
re_path(r'ws/messageboard/(?P<room_name>\w+)/$', consumers.BoardConsumer.as_asgi()),
]