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
from django.urls import path, include
from database.views import (task_list, task_form,
                            task_create, task_delete, task_complete)

urlpatterns = [
    path('', task_list),
    path('taskForm/', task_form),
    path('taskCreate/', task_create),
    path('taskDelete/<task_id>', task_delete),
    path('taskComplete/<task_id>', task_complete),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls'))
]
