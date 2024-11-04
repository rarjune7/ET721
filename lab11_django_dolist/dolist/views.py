from django.shortcuts import render, redirect 
from . models import Todolist
from . forms import TodoList
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_tasks = Todolist.objects.order_by('id')
    context = {'todo_tasks' : todo_tasks}
    return render(request, 'index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)