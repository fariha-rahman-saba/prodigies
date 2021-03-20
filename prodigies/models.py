from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50, default=-1)
    time = models.CharField(max_length=50)
    url = models.URLField()
    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    created = models.DateTimeField()
    due_time = models.CharField(max_length=50, default=-1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    post = models.TextField()
    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
