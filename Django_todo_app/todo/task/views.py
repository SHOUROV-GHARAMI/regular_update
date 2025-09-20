from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
# 1. Task List
def task_list(request):
    #status filter
    status_filter = request.GET.get('status', 'all' )
    #category filter
    category_filter = request.GET.get('category', 'all' )
    tasks = Task.objects.filter(user = request.user)


    if status_filter != 'all':
        tasks = tasks.filter(is_completed = (status_filter == 'completed'))

    if category_filter != 'all':
        tasks = tasks.filter(category = category_filter)


    completed_tasks = tasks.filter(is_completed = True)
    pending_tasks = tasks.filter(is_completed = False)

    return render(request, '', {
        'completed_tasks' : completed_tasks,
        'pending_tasks' : pending_tasks,
        'status_filter' : status_filter,
        'category_filter' : category_filter
    })

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False) #here database is not save yet but model form is ready for save
            form.user = request.user
            form.save() #here database is save done
            return redirect('')
        
        else:
            form = TaskForm()
        return render(request, '', {'form' : form})
# Task Detail Page
def task_detail(request, task_id):
    task = get_object_or_404(Task, id = task_id, user = request.user)
    return render(request, '', {'task' : task})

#Task delete page 
def task_delete(request, task_id):
    task = get_object_or_404(Task, id = task_id, user = request.user)
    task.delete()
    return redirect('')

#Mark task as completed
def task_mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('')
#User register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.changed_data.get('password')
            user = authenticate(username=username, password=password)
            login(user)
            return redirect('')
        else:
            form = UserCreationForm()
        return render(request, '', {'form' : form})
    



