from django.shortcuts import render, redirect
from django.http import HttpResponse


def hello_world(reques, name):
    return HttpResponse(f"<h1>Привет {name}!</h1>")


# http://127.0.0.1:8000/add/128/56
def add(request, n1, n2):
    try:
        result = int(n1) + int(n2)
        return HttpResponse(f"{result}")
    except ValueError:
        return HttpResponse("None")


# http://127.0.0.1:8000/plus?a=8&b=2
def plus(request):
    try:
        a, b = (request.GET.get('a', 0),
                request.GET.get('b', 0))
        result = int(a) + int(b)
        return HttpResponse(f"{result}")
    except ValueError:
        return HttpResponse("None")
