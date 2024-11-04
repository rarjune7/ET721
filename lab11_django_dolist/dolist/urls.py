from django.urls import path
from .  import views 

urlpatterns = [
    #load page of the app will be sent to the 'index.html' file 
    path("", views.index, name = 'index'),

    # add new task into the list
    path ('add', views.addTodoItem, name = 'add'), 

    #mark a task as completed
    path('completed/<todo_id>', views.completedTodo, name = 'completed' ),
         
]