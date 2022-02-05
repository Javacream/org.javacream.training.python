from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('<str:board_name>/', views.board, name='messageboard'),
]
