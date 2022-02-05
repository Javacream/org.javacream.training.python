from django.urls import re_path, path
from . import consumers
websocket_urlpatterns = [
#re_path(r'ws/training/Hugo/$', consumers.SimpleConsumer.as_asgi()),
path(r'ws/training/<str:s>/', consumers.SimpleConsumer.as_asgi())
]