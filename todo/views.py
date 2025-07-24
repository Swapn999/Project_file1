from django.shortcuts import render, redirect
from .models import TO_DO_LIST

def home(request):
    todos = TO_DO_LIST.objects.all()
    return render(request, 'home.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        TO_DO_LIST.objects.create(task=task)
    return redirect('home')

def complete_todo(request, todo_id):
    todo = TO_DO_LIST.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('home')

def delete_todo(request, todo_id):
    todo = TO_DO_LIST.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')
