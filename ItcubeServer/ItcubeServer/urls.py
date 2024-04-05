"""
Конфигурация URL для проекта ItcubeServer.

Список `urlpatterns` направляет URL к представлениям. Для получения дополнительной информации см:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Примеры:
Представления функций
    1. Добавьте импорт: from my_app import views
    2. Добавьте URL в urlpatterns: path('', views.home, name='home')
Представления на основе классов
    1. Добавьте импорт: from other_app.views import Home
    2. Добавьте URL в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Импортируем функцию include(): from django.urls import include, path
    2. Добавьте URL в urlpatterns: path('blog/', include('blog.urls'))
"""
# https://github.com/viltskaa/djangoTest/blob/main/itcubeSite/command.txt

from django.contrib import admin
from django.urls import path
from ItcubeServer.views.input_views import registration, profile, list_users
from ItcubeServer.views.views import main

urlpatterns = [
    path('', main),
    path('profile/', profile),
    path('list/', list_users),
    path('admin/', admin.site.urls)
]
