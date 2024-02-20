from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    author_ip = models.CharField(max_length=100)
