from django.shortcuts import render, redirect
from database.models import User
from django.http import HttpResponse


def registration(request):
    return render(request, "input_test.html")


def profile(request):
    args = request.GET

    login = args.get('email')
    password = args.get('password')
    password_confirm = args.get('password_confirm')

    if password != password_confirm:
        return redirect('')

    birthday = args.get('birthday')
    gender = args.get('gender')

    user = User(
        login=login,
        password=password,
        gender=gender,
        bithdate=birthday
    )

    user.save()

    return render(request, "profile.html", {
        "email": login,
        "password": password,
        "birthday": birthday,
        "gender": gender
    })


def list_users(request):
    users = User.objects.all()
    result = []

    for user in users:
        result.append((
            user.id,
            user.login,
            user.password,
            user.gender,
            user.confirm
        ))

    return render(request, "users.html", {
        "users": result
    })