from django.urls import path
from . import views

app_name = 'upload_notes'

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('upload/', views.upload_note_image, name='upload_note_image'),
]
