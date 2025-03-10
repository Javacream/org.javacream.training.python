from django.urls import path
from .views import echo_view
urlpatterns = [
    path('echo/', echo_view, name='echo')

]