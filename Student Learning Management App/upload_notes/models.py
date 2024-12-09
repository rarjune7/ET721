from django.db import models

class Note(models.Model):
    subject = models.CharField(max_length=255)
    image = models.ImageField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
