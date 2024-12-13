from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_notes_list, name='upload_notes_list'),
    path('create/', views.upload_notes_create, name='upload_notes_create'),
]
