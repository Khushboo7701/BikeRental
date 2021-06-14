from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bikes/', views.bikes, name='bikes'),
    path('book/<slug:slug_text>/', views.book, name='book'),
    path('history/', views.history, name='history'),
    path('book/confirm/<slug:slug_text>/', views.confirm, name='confirm'),
    ]

