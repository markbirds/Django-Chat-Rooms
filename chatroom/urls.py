# chat_app/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:roomname>/<str:user>/<str:user_id>/', views.rooms, name='rooms'),
]