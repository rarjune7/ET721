from django.shortcuts import render, redirect
from .models import NoteImage

def note_list(request):
    notes = NoteImage.objects.all()
    return render(request, 'upload_notes/note_list.html', {'notes': notes})

def upload_note_image(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        image = request.FILES['image']
        NoteImage.objects.create(title=title, category=category, image=image)
        return redirect('upload_notes:note_list')
    return render(request, 'upload_notes/upload_note_image.html')
