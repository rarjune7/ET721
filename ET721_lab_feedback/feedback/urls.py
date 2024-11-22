from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('items/', views.item_list, name='item_list'),  # URL for viewing all items
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
]
