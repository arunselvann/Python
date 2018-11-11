from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm

def login_view(requests):
    title = 'login'
    form = UserLoginForm(requests.POST or None)
    next = requests.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(requests, user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(requests, 'accounts/form.html', {'title': title, 'form': form})


def register_view(requests):
    title = 'Register'
    form = UserRegisterForm(requests.POST or None)
    next = requests.GET.get('next')
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(requests, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
        'title': title
    }
    return render(requests, 'accounts/form.html', context)


def logout_view(requests):
    logout(requests)
    return redirect('/')