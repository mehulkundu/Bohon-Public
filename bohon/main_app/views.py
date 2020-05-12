from django.shortcuts import render
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import MySignUpForm
# Create your views here.


class MySignUpView(CreateView):
    form_class = MySignUpForm
    template_name = "main_app/user_signup_form.html"
    success_url = reverse_lazy('user_login')


def user_home_view(request):
    template_name = "main_app/user_home.html"
    context = {}
    return render(request, template_name, context)


def rate_calculator_view(request):
    template_name = "main_app/rate_calculator1.html"
    context = {}
    return render(request, template_name, context)


class AllOptionsList(ListView):
	model = Product