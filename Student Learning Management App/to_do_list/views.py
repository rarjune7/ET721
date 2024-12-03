from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'to_do_list/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        category = request.POST['category']
        due_date = request.POST['due_date']
        Task.objects.create(title=title, description=description, category=category, due_date=due_date)
        return redirect('to_do_list:task_list')
    return render(request, 'to_do_list/add_task.html')

def mark_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('to_do_list:task_list')
