import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import training.routing
from asgi_cors import asgi_cors
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'training_channels.settings')

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
        training.routing.websocket_urlpatterns
      )
   ),
})
#application = asgi_cors(application, allow_all=True)