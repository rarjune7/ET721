# upload_notes/forms.py
from django import forms
from .models import UploadNote  # Corrected import

class UploadNotesForm(forms.ModelForm):  # You can keep the form class name as UploadNotesForm
    class Meta:
        model = UploadNote  # Ensure this references UploadNote
        fields = ['file', 'description']
