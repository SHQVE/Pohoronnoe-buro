from django.shortcuts import render, redirect
from .models import Car

import datetime


def car_list(request):
    cars = Car.objects.all()
    result = []

    for car in cars:
        result.append((
            car.id,
            car.company,
            car.brand,
            car.body,
            car.type,
            car.weight,
            car.price,
            car.levy,
            car.author,
            car.date,
            car.color,
            car.horse_power
        ))

    return render(request, 'carList.html', {
        'cars': result
    })


def car_form(request):
    return render(request, 'carForm.html')


def car_create(request):
    args = request.GET

    company = args.get('company', "")
    brand = args.get('brand', "")
    price = args.get('price', 0)
    type = args.get('type', "")
    weight = args.get('weight', 0)
    body = args.get('body', "")
    horse_power = args.get('horsePower', 0)
    author = args.get('author')
    date = args.get('date')
    color = args.get('color')

    # task = Task(text=text,
    #             author=request.user,
    #             date=date)
    # task.save()
    car = Car(
        company=company,
        brand=brand,
        price=price,
        type=type,
        weight=weight,
        body=body,
        horse_power=horse_power,
        levy=int(horse_power) * 0.3,
        author=request.user,
        date=datetime.date.today(),
        color=color
    )
    car.save()

    return redirect("/")


def car_delete(request, car_id):
    Car.objects.filter(id=car_id).delete()
    return redirect("/")


def car_complete(request, car_id):
    car = Car.objects.get(id=car_id)

    car.implementer = request.user
    car.date_implementation = datetime.datetime.now().date()
    car.checked = True
    car.save()

    return redirect("/")
