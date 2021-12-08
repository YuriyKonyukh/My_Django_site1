from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def index(request):
    tasks = Task.objects.order_by('id')  # .order_by('id' // 'title' // 'task') - сортировка по названиям
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def feedback(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Please, enter correct information'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/feedback.html', context)


def projects(request):
    return render(request, 'main/projects.html')