from django.forms import ModelForm
from . models import Todo, Post


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'due_time']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['memo']
