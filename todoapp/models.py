from django.db import models

# Create your models here.
class todoList(models.Model):
    content=models.TextField()
    