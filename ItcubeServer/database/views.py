from django.shortcuts import render, redirect
from .models import Task

import datetime


def task_list(request):
    tasks = Task.objects.all()
    result = []

    for task in tasks:
        result.append((
            task.id,
            task.text,
            task.date,
            task.author,
            task.checked,
            task.implementer,
            task.date_implementation
        ))

    return render(request, 'taskList.html', {
        'tasks': result
    })


def task_form(request):
    return render(request, 'taskForm.html')


def task_create(request):
    args = request.GET

    text = args.get('text', '')
    date = args.get('date', '')

    task = Task(text=text,
                author=request.user,
                date=date)
    task.save()

    return redirect("/")


def task_delete(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect("/")


def task_complete(request, task_id):
    task = Task.objects.get(id=task_id)

    task.implementer = request.user
    task.date_implementation = datetime.datetime.now().date()
    task.checked = True
    task.save()

    return redirect("/")
