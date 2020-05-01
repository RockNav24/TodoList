from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
