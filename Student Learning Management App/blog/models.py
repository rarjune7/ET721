from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('tips', 'Tips'),
        ('projects', 'Projects'),
        ('experiences', 'Experiences'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
