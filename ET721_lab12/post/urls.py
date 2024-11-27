from .views import HomePageView, CreatePostView  # Fixed typo in HomePageView
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Correct case for HomePageView
    path('post', CreatePostView.as_view(), name='add_post'),
]
