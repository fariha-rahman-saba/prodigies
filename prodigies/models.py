from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # link = models.URLField(blank=True)
    due_time = models.DateField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Post(models.Model):
    post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
