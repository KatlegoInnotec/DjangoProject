from tkinter.constants import CASCADE

from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=250)

    def __str__(self):
        return self.topic


class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.TextField()
    article = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
        comment =models.TextField()

        def __str__(self):
            return self.comment

