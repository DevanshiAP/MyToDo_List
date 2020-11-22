from django.db import models

# Create your models here.

class Todolist(models.Model):
    todo = models.CharField('To Do List',max_length=500)
    date = models.DateTimeField(auto_now_add=True)
