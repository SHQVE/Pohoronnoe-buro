from django.shortcuts import render, redirect
from django.http import HttpResponse


# http://127.0.0.1:8000/hello/name
def hello_world(request, name):
    return render(request, "test.html", {
        "name": name
    })


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


def parabola_view(request):
    return render(request, "parabola_form.html")


# http://127.0.0.1:8000/parabola/?a=5&b=6&c=3
def parabola(request):
    try:
        a, b, c = map(float, [request.GET.get('a', 0),
                              request.GET.get('b', 0),
                              request.GET.get('c', 0)])
        x = -b / (2 * a)
        y = a * x ** 2 + b * x + c

        return render(request, 'parabola.html', {
            "a": a,
            "b": b,
            "c": c,
            "x": round(x, 2),
            "y": round(y, 2)
        })
    except ValueError as e:
        return render(request, 'argument_error.html', {
            "text": e
        })

# http://127.0.0.1:8000/minus?a=8&b=2
# http://127.0.0.1:8000/mul?a=8&b=2
# http://127.0.0.1:8000/div?a=8&b=2
# http://127.0.0.1:8000/sin?x=89
