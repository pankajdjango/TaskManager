from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return self.title
