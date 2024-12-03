from django.db import models

class NoteImage(models.Model):
    image = models.ImageField(upload_to='notes/')
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('math', 'Math'),
        ('science', 'Science'),
        ('history', 'History'),
    ])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
