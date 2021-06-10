from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bikes/', views.bikes, name='bikes'),
    path('book/<int:b_id>/', views.book, name='book'),
    path('history/', views.history, name='history'),
    path('book/confirm/<int:b_id>/', views.confirm, name='confirm'),
    ]