from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')

    tasks = Task.objects.all()
    return render(request, 'hello/home.html', {'tasks': tasks})