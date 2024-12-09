from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('personal', 'Personal'),
        ('deadline', 'Deadline'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='academic')
    due_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
