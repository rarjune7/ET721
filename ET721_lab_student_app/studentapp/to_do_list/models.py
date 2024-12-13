# to_do_list/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(default='2024-12-13')  # Set your default date here
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
