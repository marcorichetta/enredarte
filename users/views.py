from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.shortcuts import redirect


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/register.html"


def choice_homepage(request):
    """ Redirigir a una página de inicio diferente en función del tipo de usuario """

    user = request.user

    operario = user.groups.filter(name="grupo_operario")

    if operario:
        return redirect("pedidos:ordenes")

    return redirect("core:home")
