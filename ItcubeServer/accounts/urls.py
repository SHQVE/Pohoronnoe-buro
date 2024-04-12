from django.urls import path

from .views import Reg

urlpatterns = [
    path('reg/', Reg.as_view(), name='signup')
]