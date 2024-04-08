from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    result = []

    for task in tasks:
        result.append((
            task.id,
            task.text,
            task.date,
            task.person
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
    person = args.get('person', 'default')

    task = Task(text=text, person=person, date=date)
    task.save()

    return redirect("/")


def task_delete(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect("/")
