from django.shortcuts import render
from django.template import context

def login(request):
    context = {
        'title':'Home - Авторизація',
    }
    return render(request, 'users/login.html', context)

def register(request):
    context = {
        'title':'Home - Реєстрація',
    }
    return render(request, 'users/register.html', context)

def profile(request):
    context = {
        'title':'Home - Кабінет',
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    pass
