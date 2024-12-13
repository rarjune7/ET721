from django import forms
from .models import Task  # Assuming you have a Task model

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'category']
