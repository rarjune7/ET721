from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'to_do_list/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list view
    else:
        form = TaskForm()
    return render(request, 'to_do_list/task_form.html', {'form': form})

# to_do_list/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_edit(request, id):
    task = get_object_or_404(Task, id=id)  # Retrieve the task object
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save the updated task
            return redirect('task_list')  # Redirect to the task list page
    else:
        form = TaskForm(instance=task)
    return render(request, 'to_do_list/task_form.html', {'form': form})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)  # Retrieve the task object
    if request.method == 'POST':  # Use POST method for deletion
        task.delete()  # Delete the task
        return redirect('task_list')  # Redirect to the task list page
    return render(request, 'to_do_list/task_confirm_delete.html', {'task': task})






