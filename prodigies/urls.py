from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo, name='todo'),
    path('', views.post, name='post'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_todo/<todo_id>', views.todo_ud, name='edit_todo'),
    path('edit_post/<post_id>', views.todo_ud, name='edit_post'),
]
