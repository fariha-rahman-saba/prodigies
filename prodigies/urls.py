from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('todo/', views.todo, name='todo'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_todo/<todo_id>', views.todo_ud, name='edit_todo'),
    path('edit_post/<post_id>', views.post_ud, name='edit_post'),
    path('myposts/', views.myposts, name='myposts'),
    path('mytodos/', views.mytodos, name='mytodos'),
    path('delete_todo/<todo_id>',views.delete_todo,name='todo_delete'),
    path('delete_post/<post_id>',views.delete_post,name='post_delete'),
]
