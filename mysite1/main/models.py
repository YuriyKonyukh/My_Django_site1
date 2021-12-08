from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField('Name_of_title', max_length=50)
    task = models.TextField('Name_of_task', max_length=200)

    def __str__(self):
        return self.title
