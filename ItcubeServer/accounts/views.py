from django.contrib import auth
from django.urls import reverse_lazy
from django.views import generic


class Reg(generic.CreateView):
    form_class = auth.forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "sign_up.html"

