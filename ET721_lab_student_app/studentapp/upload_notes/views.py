from django.shortcuts import render, redirect
from .models import UploadNote
from .forms import UploadNotesForm

def upload_notes_list(request):
    notes = UploadNote.objects.all()
    return render(request, 'upload_notes/upload_notes_list.html', {'notes': notes})

def upload_notes_create(request):
    if request.method == 'POST':
        form = UploadNotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_notes_list')
    else:
        form = UploadNotesForm()
    return render(request, 'upload_notes/upload_notes_form.html', {'form': form})






