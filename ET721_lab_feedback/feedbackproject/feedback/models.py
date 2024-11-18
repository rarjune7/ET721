from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="feedbacks")
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.rating}"
