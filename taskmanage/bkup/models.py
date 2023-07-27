from django.db import models

# Create your models here.

class Tasksm(models.Model):
    taskname = models.CharField(max_length=100)
    taskpriority = models.CharField(max_length=3)
    date = models.CharField(max_length=15)

    #POST PUT DELETE GET
