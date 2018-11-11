from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, SignUp_F, UserRegistrationForm
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import user
from django.http import HttpResponse


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, 'registration/login.html', {'form': form})

def signup_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
    return render(request,'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request,'registration/login.html', {})