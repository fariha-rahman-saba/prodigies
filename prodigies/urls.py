from django.urls import path
from . import views

urlpatterns = [
    path('', views.meeting, name='home'),
    path('todo/', views.todo, name='todo'),
    path('post/', views.post, name='post'),
    path('create_class/', views.create_class, name='create_class'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('create_post/', views.create_post, name='create_post'),
]
